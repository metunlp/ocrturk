from __future__ import annotations

import re
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

import pandas as pd
import numpy as np
from PIL import Image
from bs4 import BeautifulSoup
import torch

import Levenshtein


@dataclass(frozen=True)
class PathConfig:
    ground_truth_root: Path
    model_outputs_root: Path
    results_root: Path = Path("./eval_results")
    markdown_ext: str = ".md"



@dataclass(frozen=True)
class EvalConfig:
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    recursive: bool = True

    lowercase: bool = True
    normalize_whitespace: bool = True

    parse_html_tables: bool = True
    parse_markdown_tables: bool = True

    # Image metrics
    run_images: bool = True
    image_exts: Tuple[str, ...] = (".png", ".jpg", ".jpeg", ".webp")

    # Extra image metrics (optional)
    run_lpips: bool = False
    lpips_net: str = "alex"  # alex | vgg | squeeze
    run_dreamsim: bool = True  # default False to avoid scipy issues
    dreamsim_type: str = "ensemble"
    dreamsim_cache_dir: Optional[Path] = None

    # PSNR / SSIM
    run_psnr: bool = True
    run_ssim: bool = True

    # Image resizing policy
    resize_to_square: Optional[int] = None  # if set, resize both to NxN
    if_sizes_differ_resize_my_to_gt: bool = True

    # Pairing policy
    allow_basename_fallback: bool = True

    # Text metrics
    run_bleu: bool = True
    bleu_n: int = 4
    run_turkish_char_similarity: bool = True


_TURKISH_CHARS = set("çğıöşüÇĞİÖŞÜ")

def _safe_mkdir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def _norm_text(s: str, cfg: EvalConfig) -> str:
    if s is None:
        return ""
    if cfg.lowercase:
        s = s.lower()
    if cfg.normalize_whitespace:
        s = re.sub(r"\s+", " ", s).strip()
    return s

def _lev_distance(a: str, b: str) -> int:
    return int(Levenshtein.distance(a, b))

def _ned_similarity(a: str, b: str, cfg: EvalConfig) -> float:
    a = _norm_text(a, cfg)
    b = _norm_text(b, cfg)
    if not a and not b:
        return 0.0
    denom = max(len(a), len(b))
    if denom == 0:
        return 0.0
    dist = _lev_distance(a, b)
    return float(dist / denom)

def _turkish_char_similarity(ref: str, hyp: str, cfg: EvalConfig) -> float:
    ref_n = _norm_text(ref, cfg)
    hyp_n = _norm_text(hyp, cfg)

    N = sum(1 for ch in ref_n if ch in _TURKISH_CHARS)
    if N == 0:
        return 1.0

    import difflib
    sm = difflib.SequenceMatcher(a=ref_n, b=hyp_n)
    E = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        if tag in ("delete", "replace"):
            E += sum(1 for ch in ref_n[i1:i2] if ch in _TURKISH_CHARS)
        if tag in ("insert", "replace"):
            E += sum(1 for ch in hyp_n[j1:j2] if ch in _TURKISH_CHARS)

    return float(max(0.0, 1.0 - (E / N)))


_eq_tok_pat = re.compile(r"(\\[A-Za-z]+)|([A-Za-z]+)|(\d+)|(\S)")

def _tokenize_equation(s: str) -> List[str]:
    s = s or ""
    out: List[str] = []
    for m in _eq_tok_pat.finditer(s):
        tok = m.group(0)
        if tok.strip():
            out.append(tok)
    return out

def _bleu4(hyp_tokens: List[str], ref_tokens: List[str]) -> float:
    if not ref_tokens and not hyp_tokens:
        return 1.0
    if not ref_tokens or not hyp_tokens:
        return 0.0

    def ngrams(tokens: List[str], n: int) -> Dict[Tuple[str, ...], int]:
        d: Dict[Tuple[str, ...], int] = {}
        for i in range(len(tokens) - n + 1):
            g = tuple(tokens[i:i+n])
            d[g] = d.get(g, 0) + 1
        return d

    precisions = []
    for n in (1, 2, 3, 4):
        hyp_ng = ngrams(hyp_tokens, n)
        ref_ng = ngrams(ref_tokens, n)
        match = 0
        total = 0
        for g, c in hyp_ng.items():
            total += c
            match += min(c, ref_ng.get(g, 0))
        p = (match + 1.0) / (total + 1.0)
        precisions.append(p)

    hyp_len = len(hyp_tokens)
    ref_len = len(ref_tokens)
    if hyp_len == 0:
        return 0.0
    bp = 1.0 if hyp_len > ref_len else math.exp(1.0 - (ref_len / hyp_len))

    score = bp * math.exp(sum((1/4) * math.log(p) for p in precisions))
    return float(score)

def _cdm(ref: str, hyp: str) -> float:
    ref = ref or ""
    hyp = hyp or ""
    import difflib
    sm = difflib.SequenceMatcher(a=ref, b=hyp)
    TP = FP = FN = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            TP += (i2 - i1)
        elif tag == "delete":
            FN += (i2 - i1)
        elif tag == "insert":
            FP += (j2 - j1)
        elif tag == "replace":
            FN += (i2 - i1)
            FP += (j2 - j1)
    denom = (2 * TP + FP + FN)
    return 1.0 if denom == 0 else float((2 * TP) / denom)


@dataclass
class ExtractedMarkdown:
    path: Path
    raw: str
    text: str
    equations: List[str]
    tables: List[pd.DataFrame]
    image_refs: List[str]

class MarkdownExtractor:
    _img_pat = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
    _html_img_pat = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.IGNORECASE)
    _latex_block_pat = re.compile(r"\$\$(.*?)\$\$", re.DOTALL)
    _latex_bracket_pat = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)
    _latex_paren_pat = re.compile(r"\\\((.*?)\\\)", re.DOTALL)

    def extract(self, md_path: Path, cfg: EvalConfig) -> ExtractedMarkdown:
        raw = md_path.read_text(encoding="utf-8", errors="ignore")
        image_refs = self._extract_images(raw)
        equations = self._extract_equations(raw)

        tables: List[pd.DataFrame] = []
        if cfg.parse_html_tables:
            tables.extend(self._extract_html_tables(raw))
        if cfg.parse_markdown_tables:
            tables.extend(self._extract_markdown_tables(raw))

        text = self._extract_plain_text(raw)

        return ExtractedMarkdown(
            path=md_path,
            raw=raw,
            text=text,
            equations=equations,
            tables=tables,
            image_refs=image_refs,
        )

    def _extract_images(self, raw: str) -> List[str]:
        out = []
        # Extract markdown-style images: ![alt](path)
        for m in self._img_pat.finditer(raw):
            ref = m.group(1).strip()
            if ref.count('"') >= 2:
                ref = ref.split('"')[0].strip()
            out.append(ref)
        
        # Extract HTML-style images: <img src="path">
        for m in self._html_img_pat.finditer(raw):
            ref = m.group(1).strip()
            out.append(ref)
        
        return out

    def _extract_equations(self, raw: str) -> List[str]:
        eqs = []
        for pat in (self._latex_block_pat, self._latex_bracket_pat, self._latex_paren_pat):
            for m in pat.finditer(raw):
                eqs.append(m.group(1).strip())
        return eqs

    def _extract_html_tables(self, raw: str) -> List[pd.DataFrame]:
        if "<table" not in raw.lower():
            return []
        soup = BeautifulSoup(raw, "lxml")
        tables = soup.find_all("table")
        out = []
        for t in tables:
            try:
                from io import StringIO
                dfs = pd.read_html(StringIO(str(t)))
                out.extend(dfs)
            except Exception:
                continue
        return out

    def _extract_markdown_tables(self, raw: str) -> List[pd.DataFrame]:
        lines = raw.splitlines()
        out: List[pd.DataFrame] = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if "|" in line:
                if i + 1 < len(lines) and re.match(r"^\s*\|?[\s:\-|]+\|?\s*$", lines[i + 1]):
                    block = [lines[i], lines[i + 1]]
                    j = i + 2
                    while j < len(lines) and "|" in lines[j] and lines[j].strip() != "":
                        block.append(lines[j])
                        j += 1
                    df = self._pipe_block_to_df(block)
                    if df is not None:
                        out.append(df)
                    i = j
                    continue
            i += 1
        return out

    def _pipe_block_to_df(self, block: List[str]) -> Optional[pd.DataFrame]:
        try:
            header = [c.strip() for c in block[0].strip().strip("|").split("|")]
            rows = []
            for rowline in block[2:]:
                row = [c.strip() for c in rowline.strip().strip("|").split("|")]
                rows.append(row)

            width = len(header)
            norm_rows = []
            for r in rows:
                if len(r) < width:
                    r = r + [""] * (width - len(r))
                elif len(r) > width:
                    r = r[:width]
                norm_rows.append(r)

            return pd.DataFrame(norm_rows, columns=header)
        except Exception:
            return None

    def _extract_plain_text(self, raw: str) -> str:
        raw2 = re.sub(r"```.*?```", " ", raw, flags=re.DOTALL)
        raw2 = self._img_pat.sub(" ", raw2)
        raw2 = re.sub(r"<[^>]+>", " ", raw2)
        raw2 = self._latex_block_pat.sub(" ", raw2)
        raw2 = self._latex_bracket_pat.sub(" ", raw2)
        raw2 = self._latex_paren_pat.sub(" ", raw2)
        raw2 = re.sub(r"^\s*\|?[\s:\-|]+\|?\s*$", " ", raw2, flags=re.MULTILINE)
        return raw2


def _df_to_norm_string(df: pd.DataFrame, cfg: EvalConfig) -> str:
    df2 = df.copy()
    df2.columns = [str(c) for c in df2.columns]
    df2 = df2.fillna("")
    return _norm_text(df2.to_csv(index=False), cfg)

def _tables_ned(gt_tables: List[pd.DataFrame], my_tables: List[pd.DataFrame], cfg: EvalConfig) -> float:
    if not gt_tables and not my_tables:
        return 0.0
    if not gt_tables or not my_tables:
        return 1.0
    k = min(len(gt_tables), len(my_tables))
    sims = []
    for i in range(k):
        sims.append(_ned_similarity(_df_to_norm_string(gt_tables[i], cfg), _df_to_norm_string(my_tables[i], cfg), cfg))
    return float(np.mean(sims)) if sims else 0.0

def _lev_seq_distance(a: List[str], b: List[str], sub_cost_fn) -> float:
    n, m = len(a), len(b)
    dp = [[0.0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = float(i)
    for j in range(1, m+1):
        dp[0][j] = float(j)
    for i in range(1, n+1):
        for j in range(1, m+1):
            sub = dp[i-1][j-1] + sub_cost_fn(a[i-1], b[j-1])
            dele = dp[i-1][j] + 1.0
            ins = dp[i][j-1] + 1.0
            dp[i][j] = min(sub, dele, ins)
    return dp[n][m]

def _ssim_numpy(a01: np.ndarray, b01: np.ndarray) -> float:
    if a01.ndim == 3:
        ax = a01.mean(axis=2)
        bx = b01.mean(axis=2)
    else:
        ax, bx = a01, b01

    mu_x = ax.mean()
    mu_y = bx.mean()
    var_x = ((ax - mu_x) ** 2).mean()
    var_y = ((bx - mu_y) ** 2).mean()
    cov_xy = ((ax - mu_x) * (bx - mu_y)).mean()

    c1 = (0.01 ** 2)
    c2 = (0.03 ** 2)

    num = (2 * mu_x * mu_y + c1) * (2 * cov_xy + c2)
    den = (mu_x ** 2 + mu_y ** 2 + c1) * (var_x + var_y + c2)
    return float(num / den) if den != 0 else 0.0


def _tables_teds_like(gt_tables: List[pd.DataFrame], my_tables: List[pd.DataFrame], cfg: EvalConfig) -> float:
    if not gt_tables and not my_tables:
        return 1.0
    if not gt_tables or not my_tables:
        return 0.0

    k = min(len(gt_tables), len(my_tables))
    sims: List[float] = []
    for i in range(k):
        gt = gt_tables[i].fillna("").astype(str)
        my = my_tables[i].fillna("").astype(str)

        gt_rows = [" | ".join(r.tolist()) for _, r in gt.iterrows()]
        my_rows = [" | ".join(r.tolist()) for _, r in my.iterrows()]

        if not gt_rows and not my_rows:
            sims.append(1.0)
            continue
        if not gt_rows or not my_rows:
            sims.append(0.0)
            continue

        def sub_cost(x: str, y: str) -> float:
            return float(1.0 - _ned_similarity(x, y, cfg))

        dist = _lev_seq_distance(gt_rows, my_rows, sub_cost)
        denom = max(len(gt_rows), len(my_rows))
        sims.append(float(1.0 - (dist / denom if denom else 0.0)))

    return float(np.mean(sims)) if sims else 0.0


class ImageMetrics:
    def __init__(self, cfg: EvalConfig):
        self.cfg = cfg
        self.device = torch.device(cfg.device)
        self._lpips = None
        self._dreamsim_model = None
        self._dreamsim_preprocess = None

        if cfg.run_dreamsim:
            try:
                print("[INFO] Initializing DreamSim model...")
                from dreamsim import dreamsim  # type: ignore
                
                # Use a writable cache directory
                if cfg.dreamsim_cache_dir:
                    cache_dir = Path(cfg.dreamsim_cache_dir)
                else:
                    # Use home directory cache instead of /content
                    cache_dir = Path.home() / ".cache" / "dreamsim"
                
                cache_dir.mkdir(parents=True, exist_ok=True)
                print(f"[INFO] DreamSim cache directory: {cache_dir}")

                res = dreamsim(
                    pretrained=True,
                    dreamsim_type=cfg.dreamsim_type,
                    device=str(self.device),
                    cache_dir=str(cache_dir),
                )
                if isinstance(res, tuple) and len(res) >= 2:
                    model, preprocess = res[0], res[1]
                else:
                    model, preprocess = res, None

                if hasattr(model, "eval"):
                    model = model.eval()

                self._dreamsim_model = model
                self._dreamsim_preprocess = preprocess
                print("[INFO] ✓ DreamSim initialized successfully")
            except Exception as e:
                print(f"[ERROR] DreamSim disabled (initialization failed): {e}")
                print("[ERROR] Image metrics will only include MSE")
                self._dreamsim_model = None
                self._dreamsim_preprocess = None

    @staticmethod
    def _pil_to_np01(img: Image.Image) -> np.ndarray:
        return np.asarray(img).astype(np.float32) / 255.0

    @staticmethod
    def _pil_to_torch_01(img: Image.Image) -> torch.Tensor:
        arr = np.asarray(img).astype(np.float32) / 255.0
        return torch.from_numpy(arr).permute(2, 0, 1).unsqueeze(0)

    @staticmethod
    def _to_minus1_1(t01: torch.Tensor) -> torch.Tensor:
        return t01 * 2.0 - 1.0

    def _prepare_pair(self, gt_path: Path, my_path: Path) -> Tuple[Image.Image, Image.Image]:
        gt = Image.open(gt_path).convert("RGB")
        my = Image.open(my_path).convert("RGB")

        if self.cfg.resize_to_square is not None:
            n = self.cfg.resize_to_square
            gt = gt.resize((n, n), Image.BILINEAR)
            my = my.resize((n, n), Image.BILINEAR)
        elif self.cfg.if_sizes_differ_resize_my_to_gt and (gt.size != my.size):
            my = my.resize(gt.size, Image.BILINEAR)

        return gt, my

    def compute(self, gt_path: Path, my_path: Path) -> Dict[str, float]:
        gt_img, my_img = self._prepare_pair(gt_path, my_path)

        gt_np = self._pil_to_np01(gt_img)
        my_np = self._pil_to_np01(my_img)

        out: Dict[str, float] = {}
        mse = float(np.mean((gt_np - my_np) ** 2))
        out["mse"] = mse

        if self._dreamsim_model is not None and self._dreamsim_preprocess is not None:
            try:
                with torch.no_grad():
                    a = self._dreamsim_preprocess(gt_img).to(self.device)
                    b = self._dreamsim_preprocess(my_img).to(self.device)
                    d = self._dreamsim_model(a, b)
                    if hasattr(d, "item"):
                        d = d.item()
                out["dreamsim"] = float(d)
            except Exception:
                out["dreamsim"] = float("nan")

        return out


IMG_EXTS = (".png", ".jpg", ".jpeg", ".webp")

def _list_images(root: Optional[Path], image_exts: Tuple[str, ...] = IMG_EXTS) -> List[Path]:
    if root is None or (not root.exists()):
        return []
    out: List[Path] = []
    for e in image_exts:
        out.extend(root.rglob(f"*{e}"))
    return [p for p in out if p.is_file()]

def _extract_last_int(s: str) -> Optional[int]:
    nums = re.findall(r"\d+", s)
    if not nums:
        return None
    try:
        return int(nums[-1])
    except Exception:
        return None

def _find_data_dir_from_path(p: Path) -> Optional[str]:
    for part in p.parts:
        if re.fullmatch(r"data_\d+", part):
            return part
    return None

def _choose_best_image_dir(model_data_dir: Path, image_exts: Tuple[str, ...] = IMG_EXTS) -> Optional[Path]:
    if not model_data_dir.exists():
        return None
    best: Tuple[int, Optional[Path]] = (0, None)
    for d in [model_data_dir] + [x for x in model_data_dir.rglob("*") if x.is_dir()]:
        imgs = _list_images(d, image_exts)
        if len(imgs) > best[0]:
            best = (len(imgs), d)
    return best[1]

def _model_fig_dir(model_root: Path, data_dir: str, image_exts: Tuple[str, ...] = IMG_EXTS) -> Optional[Path]:
    name = model_root.name.lower()

    if any(x in name for x in ("huanyan", "nanonets", "olmocr")):
        return None

    base = model_root / data_dir

    if "deepseek" in name:
        d = base / "images"
        return d if d.exists() else _choose_best_image_dir(base, image_exts)

    if "docling" in name:
        d = base / "fig"
        return d if d.exists() else _choose_best_image_dir(base, image_exts)

    if "paddle" in name:
        d = base / "imgs"
        return d if d.exists() else _choose_best_image_dir(base, image_exts)

    return _choose_best_image_dir(base, image_exts)

def _pair_images_one_by_one(gt_imgs: List[Path], model_imgs: List[Path]) -> List[Tuple[Path, Path]]:
    if not gt_imgs or not model_imgs:
        return []

    def gt_sort(p: Path):
        i = _extract_last_int(p.stem)
        return (i is None, i if i is not None else 10**18, p.name.lower())

    def m_sort(p: Path):
        i = _extract_last_int(p.stem)
        return (i is None, i if i is not None else 10**18, p.name.lower())

    gt = sorted(gt_imgs, key=gt_sort)
    ms = sorted(model_imgs, key=m_sort)

    ms_by_name = {p.name: p for p in ms}
    used = set()
    pairs: List[Tuple[Path, Path]] = []
    rem_gt: List[Path] = []

    for g in gt:
        m = ms_by_name.get(g.name)
        if m is not None and m not in used:
            pairs.append((g, m))
            used.add(m)
        else:
            rem_gt.append(g)

    rem_ms = [m for m in ms if m not in used]
    if not rem_gt or not rem_ms:
        return pairs

    gt_idx = [(g, _extract_last_int(g.stem)) for g in rem_gt]
    ms_idx = [(m, _extract_last_int(m.stem)) for m in rem_ms]
    gt_map = {i: g for g, i in gt_idx if i is not None}
    ms_map = {i: m for m, i in ms_idx if i is not None}

    if gt_map and ms_map:
        best_off = 0
        best_hits = -1
        for off in range(-5, 6):
            hits = 0
            for gi in gt_map.keys():
                if (gi - off) in ms_map:
                    hits += 1
            if hits > best_hits:
                best_hits = hits
                best_off = off

        used2 = set()
        rem_gt2: List[Path] = []
        for g, gi in gt_idx:
            if gi is None:
                rem_gt2.append(g)
                continue
            mi = gi - best_off
            m = ms_map.get(mi)
            if m is not None and m not in used2:
                pairs.append((g, m))
                used2.add(m)
            else:
                rem_gt2.append(g)

        rem_ms2 = [m for m in rem_ms if m not in used2]
        rem_gt = rem_gt2
        rem_ms = rem_ms2

        if not rem_gt or not rem_ms:
            return pairs

    rem_gt = sorted(rem_gt, key=gt_sort)
    rem_ms = sorted(rem_ms, key=m_sort)
    for g, m in zip(rem_gt, rem_ms):
        pairs.append((g, m))

    return pairs


def _resolve_image_path(img_ref: str, base_dir: Path, image_exts: Tuple[str, ...]) -> Optional[Path]:
    """
    Resolve an image reference from markdown to an actual file path.
    Tries various strategies to find the actual image file.
    
    Args:
        img_ref: Image reference from markdown (e.g., "imgs/image.jpg" or "image.jpg")
        base_dir: Base directory to search from (e.g., "paddle/data_1/imgs")
        image_exts: Tuple of valid image extensions
    """
    if not base_dir or not base_dir.exists():
        return None
    
    # Remove any URL parameters or anchors
    img_ref = img_ref.split('?')[0].split('#')[0].strip()
    
    # Get just the filename from the reference
    basename = Path(img_ref).name
    
    # Strategy 1: Direct match - basename in base_dir
    # This handles: img_ref="imgs/image.jpg", base_dir="data_1/imgs" -> data_1/imgs/image.jpg
    candidate = base_dir / basename
    if candidate.exists() and candidate.is_file():
        return candidate
    
    # Strategy 2: Full path relative to base_dir (in case base_dir is the data dir, not imgs dir)
    # This handles: img_ref="imgs/image.jpg", base_dir="data_1" -> data_1/imgs/image.jpg
    candidate = base_dir / img_ref
    if candidate.exists() and candidate.is_file():
        return candidate
    
    # Strategy 3: Full path relative to parent (in case base_dir is imgs but ref includes imgs/)
    # This handles: img_ref="imgs/image.jpg", base_dir="data_1/imgs" -> data_1/imgs/image.jpg (via parent)
    if base_dir.parent.exists():
        candidate = base_dir.parent / img_ref
        if candidate.exists() and candidate.is_file():
            return candidate
    
    # Strategy 4: Try different extensions with the same stem
    stem = Path(img_ref).stem
    for ext in image_exts:
        candidate = base_dir / f"{stem}{ext}"
        if candidate.exists() and candidate.is_file():
            return candidate
    
    # Strategy 5: Recursively search in base_dir for basename
    for img_path in base_dir.rglob(basename):
        if img_path.is_file():
            return img_path
    
    # Strategy 6: Recursively search for stem with any extension
    for ext in image_exts:
        for img_path in base_dir.rglob(f"{stem}{ext}"):
            if img_path.is_file():
                return img_path
    
    return None


def _pair_images_by_markdown_order(
    gt_image_refs: List[str],
    my_image_refs: List[str],
    gt_fig_dir: Path,
    model_fig_dir: Path,
    image_exts: Tuple[str, ...]
) -> List[Tuple[Path, Path]]:
    """
    Match images based on their order of appearance in the markdown files.
    The i-th image reference in ground truth is paired with the i-th image reference in model output.
    """
    pairs: List[Tuple[Path, Path]] = []
    
    # Match by position in the markdown
    num_pairs = min(len(gt_image_refs), len(my_image_refs))
    
    for i in range(num_pairs):
        gt_ref = gt_image_refs[i]
        my_ref = my_image_refs[i]
        
        # Resolve ground truth image path
        gt_img = _resolve_image_path(gt_ref, gt_fig_dir, image_exts)
        if gt_img is None:
            continue
            
        # Resolve model output image path
        my_img = _resolve_image_path(my_ref, model_fig_dir, image_exts)
        if my_img is None:
            continue
        
        pairs.append((gt_img, my_img))
    
    return pairs


class PairFinder:
    def __init__(self, cfg: EvalConfig):
        self.cfg = cfg

    def find_markdown_pairs(self, paths: PathConfig) -> List[Tuple[Path, Path]]:
        gt_root = paths.ground_truth_root
        out_root = paths.model_outputs_root

        gt_ext = paths.markdown_ext
        model_exts = (".md", ".mmd")

        gt_files = list(gt_root.rglob(f"*{gt_ext}")) if self.cfg.recursive else list(gt_root.glob(f"*{gt_ext}"))
        pairs: List[Tuple[Path, Path]] = []

        for gt in gt_files:
            rel = gt.relative_to(gt_root)
            gt_parent_rel = rel.parent

            cand = out_root / rel
            if cand.exists():
                pairs.append((gt, cand))
                continue

            matched = False
            for e in model_exts:
                cand2 = (out_root / rel).with_suffix(e)
                if cand2.exists():
                    pairs.append((gt, cand2))
                    matched = True
                    break
            if matched:
                continue

            for e in model_exts:
                cand3 = out_root / gt_parent_rel / f"result{e}"
                if cand3.exists():
                    pairs.append((gt, cand3))
                    matched = True
                    break
            if matched:
                continue

            flat_name = rel.name
            cand4 = out_root / flat_name
            if cand4.exists():
                pairs.append((gt, cand4))
                continue

            for e in model_exts:
                cand5 = (out_root / flat_name).with_suffix(e)
                if cand5.exists():
                    pairs.append((gt, cand5))
                    matched = True
                    break
            if matched:
                continue

        return pairs


class EvaluationPipeline:
    def __init__(self, paths: PathConfig, cfg: EvalConfig):
        self.paths = paths
        self.cfg = cfg
        self.extractor = MarkdownExtractor()
        self.pair_finder = PairFinder(cfg)
        self.img_metrics = ImageMetrics(cfg) if cfg.run_images else None
        _safe_mkdir(paths.results_root)

    def run(self) -> Dict[str, pd.DataFrame]:
        print("\n" + "="*60)
        print("EVALUATION CONFIGURATION")
        print("="*60)
        print(f"Ground truth root: {self.paths.ground_truth_root}")
        print(f"Model outputs root: {self.paths.model_outputs_root}")
        print(f"Results directory: {self.paths.results_root}")
        print(f"\nEnabled metrics:")
        print(f"  - Text metrics: NED, Turkish char similarity")
        print(f"  - Equation metrics: NED, BLEU, CDM")
        print(f"  - Table metrics: NED, TEDS")
        print(f"  - Image metrics: {'ENABLED' if self.cfg.run_images else 'DISABLED'}")
        if self.cfg.run_images and self.img_metrics:
            print(f"    - MSE: ✓")
            has_dreamsim = (self.img_metrics._dreamsim_model is not None)
            print(f"    - DreamSim: {'✓' if has_dreamsim else '✗ (disabled - see error above)'}")
        print("="*60 + "\n")
        
        md_pairs = self.pair_finder.find_markdown_pairs(self.paths)
        if not md_pairs:
            print("[WARNING] No markdown pairs found!")
            empty = pd.DataFrame()
            return {"per_doc": empty, "per_image": empty, "summary": empty}
        
        print(f"[INFO] Found {len(md_pairs)} markdown file pairs to evaluate")
        
        per_doc_rows: List[Dict[str, Any]] = []
        all_image_rows: List[Dict[str, Any]] = []

        for gt_md, my_md in md_pairs:
            gt_ex = self.extractor.extract(gt_md, self.cfg)
            my_ex = self.extractor.extract(my_md, self.cfg)

            doc_rel = gt_md.relative_to(self.paths.ground_truth_root).as_posix()

            text_ned = _ned_similarity(gt_ex.text, my_ex.text, self.cfg)
            text_tcs = _turkish_char_similarity(gt_ex.text, my_ex.text, self.cfg)

            eq_ned = self._list_ned(gt_ex.equations, my_ex.equations)
            eq_bleu = self._list_equation_bleu(gt_ex.equations, my_ex.equations)
            eq_cdm = self._list_equation_cdm(gt_ex.equations, my_ex.equations)

            table_ned = _tables_ned(gt_ex.tables, my_ex.tables, self.cfg)
            table_teds = _tables_teds_like(gt_ex.tables, my_ex.tables, self.cfg)

            img_count = 0
            img_aggs: Dict[str, List[float]] = {}

            if self.cfg.run_images and self.img_metrics is not None:
                data_dir = _find_data_dir_from_path(gt_md)
                if data_dir is not None:
                    # Try multiple common image directory names for ground truth
                    gt_base = self.paths.ground_truth_root / data_dir
                    gt_fig_dir = None
                    for dir_name in ["imgs", "figures", "images", "fig"]:
                        candidate = gt_base / dir_name
                        if candidate.exists():
                            gt_fig_dir = candidate
                            print(f"[INFO] {data_dir}: Found GT image directory '{dir_name}'")
                            break
                    
                    # If no standard directory found, use the base directory
                    if gt_fig_dir is None:
                        gt_fig_dir = gt_base
                        print(f"[INFO] {data_dir}: Using base directory for GT images")
                    
                    model_fig_dir = _model_fig_dir(self.paths.model_outputs_root, data_dir, self.cfg.image_exts)
                    
                    if model_fig_dir:
                        print(f"[INFO] {data_dir}: Found model image directory at {model_fig_dir.relative_to(self.paths.model_outputs_root)}")
                    else:
                        print(f"[WARNING] {data_dir}: No model image directory found")

                    # Use markdown-order based pairing instead of filename matching
                    pairs = _pair_images_by_markdown_order(
                        gt_ex.image_refs,
                        my_ex.image_refs,
                        gt_fig_dir,
                        model_fig_dir,
                        self.cfg.image_exts
                    )
                    
                    print(f"[INFO] {data_dir}: GT has {len(gt_ex.image_refs)} image refs, Model has {len(my_ex.image_refs)} image refs")
                    print(f"[INFO] {data_dir}: Successfully paired {len(pairs)} images")

                    for gt_img, my_img in pairs:
                        try:
                            metrics = self.img_metrics.compute(gt_img, my_img)
                            img_count += 1

                            for k, v in metrics.items():
                                img_aggs.setdefault(k, []).append(float(v))

                            all_image_rows.append({
                                "doc": data_dir,
                                "gt_image": str(gt_img),
                                "my_image": str(my_img),
                                **metrics
                            })
                        except:
                            continue

            def mean_or_nan(key: str) -> float:
                vals = img_aggs.get(key, [])
                return float(np.mean(vals)) if vals else float("nan")

            row = {
                "doc": doc_rel,
                "gt_md": str(gt_md),
                "my_md": str(my_md),

                "text_ned": text_ned,
                "text_tcs": text_tcs,

                "equation_ned": eq_ned,
                "equation_bleu": eq_bleu,
                "equation_cdm": eq_cdm,

                "table_ned": table_ned,
                "table_teds": table_teds,

                "fig_count": int(img_count),
                "fig_mse_avg": mean_or_nan("mse"),
                "fig_dreamsim_avg": mean_or_nan("dreamsim"),

                "gt_num_images_ref": len(gt_ex.image_refs),
                "my_num_images_ref": len(my_ex.image_refs),
                "gt_num_tables": len(gt_ex.tables),
                "my_num_tables": len(my_ex.tables),
                "gt_num_equations": len(gt_ex.equations),
                "my_num_equations": len(my_ex.equations),
            }
            per_doc_rows.append(row)

        per_doc_df = pd.DataFrame(per_doc_rows)
        per_image_df = pd.DataFrame(all_image_rows) if all_image_rows else pd.DataFrame()
        summary_df = self._summarize(per_doc_df, per_image_df)
        
        print("\n" + "="*60)
        print("EVALUATION COMPLETE")
        print("="*60)
        print(f"Documents evaluated: {len(per_doc_df)}")
        print(f"Images evaluated: {len(per_image_df)}")
        if not per_image_df.empty:
            print(f"Image metrics computed: {', '.join(per_image_df.columns[3:])}")  # Skip doc, gt_image, my_image
        print("="*60 + "\n")

        return {"per_doc": per_doc_df, "per_image": per_image_df, "summary": summary_df}

    def _list_ned(self, gt_list: List[str], my_list: List[str]) -> float:
        if not gt_list and not my_list:
            return 0.0
        if not gt_list or not my_list:
            return 1.0
        k = min(len(gt_list), len(my_list))
        sims = [_ned_similarity(gt_list[i], my_list[i], self.cfg) for i in range(k)]
        return float(np.mean(sims)) if sims else 0.0

    def _list_equation_bleu(self, gt_list: List[str], my_list: List[str]) -> float:
        if not gt_list and not my_list:
            return 1.0
        if not gt_list or not my_list:
            return 0.0
        k = min(len(gt_list), len(my_list))
        vals = []
        for i in range(k):
            ref_t = _tokenize_equation(gt_list[i])
            hyp_t = _tokenize_equation(my_list[i])
            vals.append(_bleu4(hyp_t, ref_t))
        return float(np.mean(vals)) if vals else 0.0

    def _list_equation_cdm(self, gt_list: List[str], my_list: List[str]) -> float:
        if not gt_list and not my_list:
            return 1.0
        if not gt_list or not my_list:
            return 0.0
        k = min(len(gt_list), len(my_list))
        vals = [_cdm(gt_list[i], my_list[i]) for i in range(k)]
        return float(np.mean(vals)) if vals else 0.0

    def _summarize(self, per_doc: pd.DataFrame, per_image: pd.DataFrame) -> pd.DataFrame:
        rows: List[Dict[str, Any]] = []

        if not per_doc.empty:
            rows.append({
                "group": "markdown",
                "count": int(len(per_doc)),
                "text_ned_avg": float(per_doc["text_ned"].mean()),
                "text_tcs_avg": float(per_doc["text_tcs"].mean()),
                "equation_ned_avg": float(per_doc["equation_ned"].mean()),
                "equation_bleu_avg": float(per_doc["equation_bleu"].mean()),
                "equation_cdm_avg": float(per_doc["equation_cdm"].mean()),
                "table_ned_avg": float(per_doc["table_ned"].mean()),
                "table_teds_avg": float(per_doc["table_teds"].mean()),
                
            })
        else:
            rows.append({"group": "markdown", "count": 0})

        if per_image is not None and not per_image.empty:
            r = {"group": "images", "count": int(len(per_image))}
            for col in ["mse", "dreamsim"]:
                if col in per_image.columns:
                    r[f"{col}_avg"] = float(per_image[col].replace([np.inf, -np.inf], np.nan).mean())
            rows.append(r)
        else:
            rows.append({"group": "images", "count": 0})

        return pd.DataFrame(rows)

    def save(self, results: Dict[str, pd.DataFrame]) -> None:
        out = self.paths.results_root
        _safe_mkdir(out)

        per_doc = results.get("per_doc", pd.DataFrame())
        per_image = results.get("per_image", pd.DataFrame())
        summary = results.get("summary", pd.DataFrame())

        per_doc_path = out / "per_doc_metrics.csv"
        per_image_path = out / "per_image_metrics.csv"
        summary_path = out / "summary_metrics.csv"

        per_doc.to_csv(per_doc_path, index=False)
        per_image.to_csv(per_image_path, index=False)
        summary.to_csv(summary_path, index=False)

        print("Saved:")
        print(" -", per_doc_path)
        print(" -", per_image_path)
        print(" -", summary_path)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python api_detailed_metrics.py <ground_truth_path> <model_output_path> [results_path] [--images]")
        print("  --images: Enable image metrics computation (default: disabled)")
        sys.exit(1)
    
    ground_truth_path = sys.argv[1]
    model_output_path = sys.argv[2]    
    run_images = "--images" in sys.argv
    if run_images:
        sys.argv.remove("--images")
    
    results_path = sys.argv[3] if len(sys.argv) > 3 else "./eval_results"
    
    paths = PathConfig(
        ground_truth_root=Path(ground_truth_path),
        model_outputs_root=Path(model_output_path),
        results_root=Path(results_path),
        markdown_ext=".md",
    )
    
    cfg = EvalConfig(run_images=run_images)
    
    pipeline = EvaluationPipeline(paths, cfg)
    results = pipeline.run()
    pipeline.save(results)
    
    print("\nSummary:")
    print(results["summary"])
