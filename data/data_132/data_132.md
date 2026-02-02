ile gösterilir.

Tanım 2.16 [23] $f : \mathbb{T} \to \mathbb{R}$ fonksiyonunun **regüler** olması için gerek ve yeter şart $\mathbb{T}$ zaman skalasının tüm sağ yoğun noktalarında sağ taraflı sonlu limitlerinin, tüm sol yoğun noktalarında sol taraflı sonlu limitlerinin mevcut olmasıdır.

Tanım 2.17 [23] $f : \mathbb{T} \to \mathbb{R}$ regüler bir fonksiyon olsun. $\forall t \in \mathbb{T}^\kappa$ için $F^\Delta(t) = f(t)$ özelliğini sağlayan $F : \mathbb{T} \to \mathbb{R}$ fonksiyonuna $f : \mathbb{T} \to \mathbb{R}$ fonksiyonunun **delta anti-türevi** denir.

$f$ fonksiyonunun belirsiz $\Delta$-integrali $C$ bir keyfi sabit ve $F$, $f$ fonksiyonunun ön türevi olmak üzere

$$\int f(t)\Delta t = F(t) + C,$$

şeklinde tanımlanır. $f$ fonksiyonunun Cauchy $\Delta$-integrali** ise $\forall \tau, s \in \mathbb{T}$ için

$$\int_{\tau}^{s} f(t)\Delta t = F(s) - F(\tau),$$

olarak tanımlanır.

Teorem 2.18 [23] $a, b \in \mathbb{T}$ ve $f \in C_{rd}$ olsun.

a) $\mathbb{T} = \mathbb{R}$ için

$$\int_{a}^{b} f(t) \Delta t = \int_{a}^{b} f(t) dt,$$

b) $[a, b]$ yalnızca ayrık (izole) noktalar içeriyorsa

$$\int_{a}^{b} f(t) \Delta t = \begin{cases} \sum_{t \in [a, b)} \mu(t) f(t), & a < b \text{ ise,} \\ 0, & a = b \text{ ise,} \\ -\sum_{t \in [b, a)} \mu(t) f(t), & a > b \text{ ise,} \end{cases}$$

c) $\mathbb{T} = h\mathbb{Z} = \{hk : k \in \mathbb{Z}\}$, $h > 0$ için

$$\int_{a}^{b} f(t) \Delta t = \begin{cases} \sum_{k = \frac{a}{h}}^{\frac{b}{h}-1} f(kh)h, & a < b \text{ ise,} \\ 0, & a = b \text{ ise,} \\ -\sum_{k = \frac{b}{h}}^{\frac{a}{h}-1} f(kh)h, & a > b \text{ ise} \end{cases}$$
