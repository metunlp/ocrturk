# OCRTurk Benchmark 

A comprehensive evaluation framework for comparing OCR model outputs against ground truth data. This tool provides detailed metrics for text, equations, tables, and images extracted from documents.

## Features

- **Text Metrics**: Normalized Edit Distance (NED) and Turkish character similarity
- **Equation Metrics**: BLEU-4, Character Dice Metric (CDM), and NED for LaTeX equations
- **Table Metrics**: NED and TEDS-like similarity for extracted tables
- **Image Metrics**: MSE, PSNR, SSIM, LPIPS (optional), and DreamSim (optional)
- **Flexible Pairing**: Intelligent matching of ground truth and model output files
- **Batch Processing**: Evaluate multiple documents recursively

## Installation

### Requirements

```bash
pip install -r requirements.txt
```


## Quick Start

### Basic Usage

```bash
python eval.py <ground_truth_path> <model_output_path> <image_folder> [results_path]
```

### With Image Metrics

```bash
python eval.py <ground_truth_path> <model_output_path> <image_folder> [results_path] --images
```

### Example

```bash
python eval.py ./data/ground_truth ./data/model_outputs ./data/images ./results --images
```

## Directory Structure

### Expected Input Structure

```
ground_truth/
├── data_1/
│   ├── document.md
│   └── figures/
│       ├── figure_1.png
│       └── figure_2.png
├── data_2/
│   ├── document.md
│   └── figures/
│       └── figure_1.png
└── ...

model_outputs/
├── data_1/
│   ├── result.md (or document.md)
│   └── images/ (or fig/, imgs/)
│       ├── figure_1.png
│       └── figure_2.png
└── ...
```

### Output Structure

```
results/
├── per_doc_metrics.csv      # Metrics for each document
├── per_image_metrics.csv    # Metrics for each image pair
└── summary_metrics.csv      # Aggregated summary statistics
```

## Metrics Explained

### Text Metrics

- **NED (Normalized Edit Distance)**: Levenshtein distance normalized by length (lower is better, 0 = perfect match)
- **Turkish Character Similarity**: Specialized metric for Turkish diacritics (higher is better, 1 = perfect)

### Equation Metrics

- **BLEU-4**: Standard BLEU score for LaTeX equations (higher is better, 1 = perfect)
- **CDM (Character Dice Metric)**: F1-like metric for character overlap (higher is better, 1 = perfect)
- **Equation NED**: Edit distance for LaTeX strings (lower is better)

### Table Metrics

- **Table NED**: Edit distance on CSV-serialized tables (lower is better)
- **TEDS-like**: Tree Edit Distance-based similarity for table structure (higher is better, 1 = perfect)

### Image Metrics

- **MSE**: Mean Squared Error (lower is better)
- **PSNR**: Peak Signal-to-Noise Ratio in dB (higher is better, typical range: 20-40)
- **SSIM**: Structural Similarity Index (higher is better, range: 0-1)
- **LPIPS**: Learned Perceptual Image Patch Similarity (lower is better, optional)
- **DreamSim**: Perceptual similarity metric (lower is better, optional)

## Output Files

### per_doc_metrics.csv

Per-document metrics including:
- Text NED and Turkish character similarity
- Equation metrics (NED, BLEU, CDM)
- Table metrics (NED, TEDS)
- Image metrics (aggregated per document)
- Counts of extracted elements

### per_image_metrics.csv

Per-image-pair metrics:
- MSE, PSNR, SSIM for each image pair
- Optional LPIPS and DreamSim scores
- Source file paths

### summary_metrics.csv

Aggregated statistics across all documents and images.


## License

[Add your license here]

## Citation

If you use this tool in your research, please cite:

```bibtex
Upcoming
```

