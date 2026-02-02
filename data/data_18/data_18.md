analysis values have been reviewed and compaired with the global solar radiation calculated as the
theoretica. Results show that ANN estimation based on meteorological data can be used with 99%
accuracy in sunny and clear weather conditions and 96% in rainy and cloudy weather conditions in
determining the amount of solar radiation. The presented approach can be used to determine the
generation potential of existing and planned PV plants.

Keywords: Solar Radiation, Artificial Neural Network (ANN), Meteorological Measurement, Daily Solar Radiation

1\. Giriş

Solar radyasyon, güneşin birim alan başına
yaydığı ve elektromanyetik radyasyon şeklinde
iletilen güç olarak tanımlanır[1]. Enerji sektörü
açısından bakıldığında ise solar radyasyon
miktarı; meteorolojik araştırmalar, binalarda
kullanılan doğal aydınlatma sistemleri ve
güneşten elektrik üretiminde kullanılan
fotovoltaik sistemler gibi güneş enerjisine
bağımlı olan projelerin boyutlandırılması ve
performanslarının belirlenmesinde dikkate
alınması gereken önemli bir değişkendir.

Uydular ile gerçekleştirilen ölçümlerden
dünya dışından gelen solar radyasyon
miktarının mutlak değerinin 1361 W/m2 olduğu
ve solar radyasyon değerinin klasik
radyometrelerde gözlemlenen 1365 W/m2
değerinden önemli ölçüde düşük olması
gerektiği gözlemlenmiştir [2]. Fakat gezegen
dışından gelen solar radyasyon atmosfer ile
etkileşime girdiğinde zayıflar ve sabit olmaktan
çıkar. Bu zayıflama atmosferdeki koruyucu
madde ile etkileşime giren fotonların saçılması
veya soğrulmasından kaynaklanmaktadır.

Dünyadaki enerji ihtiyacı her geçen gün artış
göstermektedir [3]. Bu nedenle ülkeler fosil
yakıtların tükenmesine karşı önlem almak ve
daha sürdürülebilir bir dünya hedefi ile elektrik
üretiminde yenilenebilir enerji kaynaklarına
yönelmektedir. Yenilenebilir enerji kaynaları
içerisinde Fotovoltaik (PV) sistemler güneş gibi
sonsuz bir enerji kaynağına sahip olması
nedeniyle önemli bir avantaja sahiptir [4-7].
Fakat PV hücrelerin üreteceği elektrik miktarını
maruz kaldıkları solar radyasyon seviyesi
belirlemektedir.

Teknolojideki ilerlemelere rağmen PV
hücrelerin verimliliği %11-28 civarındadır [8].
Bu düşük verim dikkate alındığında, PV
hücrelerden maksimum verim elde edilebilmek
için yüksek solar radyasyon seviyesine sahip
uygun lokasyonda çalıştırılması gereklidir.

Solar radyasyon miktarı piranometre,
pyheliometre ve solar metre gibi ölçüm cihazları
yardımı ile ölçülebilmektedir. Bu cihazların
maliyetlerinin yüksek olması nedeni ile dünya
üzerindeki tüm noktalarda solar radyasyonun
deneysel olarak ölçülmesi olanaksızdır. Bu
zorluğun üstesinden gelebilmek için
meteorolojik değişkenler ve solar radyasyon
arasındaki ilişkiyi matematiksel olarak
tanımlayan modeller ileri sürülmüştür [9-20].
Sunulan bu yaklaşımlar, dünyanın güneş
çevresindeki hareketine bağlı olarak astronomi
ve geometri prensiplerini temel alarak
tasarlanmıştır.

Günümüzde kurulması planlanan PV tesislerin
ekonomik analizlerinin değerlendirilmesinde
solar radyasyonu tanımlayan bu matematiksel
yaklaşımlar ve çevresel faktörler dikkate
alınarak güvenilir bir tahmin metodolojisine
ihtiyaç duyulmaktadır [21]. Yapay Sinir Ağları
(YSA) tekniği yüksek işlem hızına sahip olması,
uygulanabilirliğinin basit ve düşük maliyet
içermesi nedeniyle tahmin uygulamalarında
oldukça popülerdir[22] ve YSA uygulamaları PV
sistemlerde farklı birçok parametrenin
tahmininde kullanılmıştır.

Bora ve arkadaşları, PV modüllerin çıkış
gücünü tahmin etmede YSA metodolojisinin
kullanılabileceğini göstermiştir[23]. Ceylan ise
gerçekleştirmiş olduğu çalışmada, Fotovoltaik
panellerde modül sıcaklığının YSA ile tahmin
edilebileceğini ileri sürmüştür [24]. Solar
radyasyonun tahmininde YSA uygulamalarını
temel alan çeşitli metotlar birçok araştırmacı
tarafından inceleme konusu olmuştur [25-37].
[25-27]’ de global solar radyasyonun (GSR) YSA
kullanılarak tahmin edilebileceği incelenerek
tartışılmıştır. [28]’de ise günlük maksimum ve
minimum hava sıcaklığı ile yağış ölçümleri
mevcut olduğunda YSA’nın günlük solar
radyasyonu tahmin etmede kullanılabileceği
gösterilmiştir. [30]’ de Suudi Arabistan’da
lokasyonu bilinen 41 radyasyon toplama
istasyonun verileri kullanılarak bilinmeyen