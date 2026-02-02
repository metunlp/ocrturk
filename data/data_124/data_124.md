$$\sum_{i=1}^{n} \left(\frac{4i^2}{n^2}\right) \frac{2}{n} = \sum_{i=1}^{n} \frac{8i^2}{n^3} = \frac{8}{n^3} \sum_{i=1}^{n} i^2 = \frac{8}{n^3} \left(\frac{n(n+1)(2n+1)}{6}\right) = \frac{8}{n^3} \left(\frac{2n^3 + 3n^2 + n}{6}\right) = \frac{16n^3 + 24n^2 + 8n}{6n^3} = \frac{8}{3} + \frac{4}{n} + \frac{4}{6n^2}$$

elde edilir. Burada $n \to \infty$ için limit

$$\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x = \lim_{n \to \infty} \left(\frac{8}{3}\right) + \lim_{n \to \infty} \left(\frac{4}{n}\right) + \lim_{n \to \infty} \left(\frac{1}{6n^2}\right) = \frac{8}{3} + 0 + 0 = \frac{8}{3}$$

Burada oluşturulan alt aralıklar bu aralıklardaki $x^*$ noktaları nasıl seçilirse seçilsin, alt aralıkların sayısı sonsuza ve genişlikleri sıfıra yaklaşırken elde edilen sonuç bir sayıya yakınsayacaktır. Bu durumda, limit işlemi $[a, b]$ aralığında tanımlı belirli integral ifadesine götürecektir.

Tanım 3.2 (Belirli İntegral)

$f(x)$, $[a, b]$ aralığında tanımlı bir fonksiyon olmak üzere bu fonksiyonun belirli integrali, limitin var olması şartıyla,

$$\int_{a}^{b} f(x) dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x$$

şeklinde verilir. Eğer limit var ise $f(x)$ fonksiyonu $[a, b]$ aralığında integrallenebilir*denir [8].

Integral sembolü, 'toplam' anlamına gelen 'sum' kelimesinin baş harfi olan $S$ harfinin stilize edilmiş şeklidir. Burada aslında yükseklikleri $f(x)$, genişlikleri $dx$ (sıfırdan büyük ama sonsuz küçük) olan temsili dikdörtgenlerin alanları toplanmaktadır [6].

Tanım 3.3 (Üst Darboux İntegrali ve Alt Darboux İntegrali)

$f$, $[a, b]$ üzerinde tanımlı ve sınırlı bir fonksiyon olsun.

$$\overline{\int_{a}^{b}} f(x) dx = \inf_{s \ge f} \left\{ \int_{a}^{b} s(x) dx: s \in M[a, b] \right\}$$

$$\underline{\int_{a}^{b}} f(x) dx = \sup_{t \le f} \left\{ \int_{a}^{b} t(x) dx: t \in M[a, b] \right\}$$

sayılarına sırası ile, Üst Darboux İntegrali ve Alt Darboux İntegrali denir [7].

Tanım 3.4 (Riemann Anlamında İntegrallenebilme)