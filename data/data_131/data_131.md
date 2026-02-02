Sonuç 3.1.2 Tanım 3.1.1'de $p = 1$ ve $n = 1$ seçilirse, Tanım 2.1.1 elde edilir.

Sonuç 3.1.3 Tanım 3.1.1'de $n = 1$ seçilirse, Tanım 2.1.2 elde edilir. Dolayısıyla her $p$-konveks fonksiyon aynı zamanda $1$-kesirli polinom $p$-konveks fonksiyondur.

$n$-kesirli polinom $p$-konveks fonksiyonunun lineerlik özelliği aşağıdaki gibidir:

Teorem 3.1.1 $n \in \mathbb{N}$ ve $p \in \mathbb{R} \setminus \{0\}$ olmak üzere $f, g : I \subseteq (0, \infty) \to \mathbb{R}$ iki $n$-kesirli polinom $p$-konveks fonksiyon olsun. Bu durumda, $x, y \in I$ ve $t \in [0, 1]$ için $f+g$ fonksiyonu $n$-kesirli polinom $p$-konvekstir.

İspat. $f$ ve $g$ iki $n$-kesirli polinom $p$-konveks fonksiyon olsunlar. Bu durumda her $x, y \in I$ ve $t \in [0, 1]$ için

$$(f+g) \left([tx^p + (1-t)y^p]^{\frac{1}{p}}\right) = \left[f \left([tx^p + (1-t)y^p]^{\frac{1}{p}}\right)\right] + \left[g \left([tx^p + (1-t)y^p]^{\frac{1}{p}}\right)\right] \le \left[ \frac{1}{n} \sum_{i=1}^{n} t^{\frac{1}{i}} f(x) + \frac{1}{n} \sum_{i=1}^{n} (1-t)^{\frac{1}{i}} f(y) \right] + \left[ \frac{1}{n} \sum_{i=1}^{n} t^{\frac{1}{i}} g(x) + \frac{1}{n} \sum_{i=1}^{n} (1-t)^{\frac{1}{i}} g(y) \right] = \frac{1}{n} \sum_{i=1}^{n} t^{\frac{1}{i}} (f+g)(x) + \frac{1}{n} \sum_{i=1}^{n} (1-t)^{\frac{1}{i}} (f+g)(y)$$

yazılır. Dolayısıyla $f+g$ fonksiyonu $n$-kesirli polinom $p$-konveks fonksiyondur.

$n$-kesirli polinom $p$-konveks fonksiyonunun skaler ile çarpım özelliği aşağıdaki gibidir:

Teorem 3.1.2 $n \in \mathbb{N}$, $\lambda \ge 0$, $p \in \mathbb{R} \setminus \{0\}$ ve $f : I \subseteq (0, \infty) \to \mathbb{R}$ negatif olmayan bir $n$-kesirli polinom $p$-konveks fonksiyon olsun. Bu durumda $\lambda f$ de bir $n$-kesirli polinom $p$-konveks fonksiyondur.

İspat. $f$ $n$-kesirli polinom $p$-konveks fonksiyon olduğunda, her $x, y \in I$ ve $t \in [0, 1]$ için

$$(\lambda f) \left([tx^p + (1-t)y^p]^{\frac{1}{p}}\right)$$