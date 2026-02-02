1. GİRİŞ
Kıyı alanları, insan etkileri ve doğal sebeplerden
kaynaklanan dinamik değişiklerin olduğu, ekonomik
ve sosyal açıdan nitelikli bölgelerdir. Mineral
kaynakları, petrol-gaz kaynakları, gelgit-dalga enerji
kaynakları ve diğer yenilenebilir enerji kaynakları
bakımından yerleşimler kıyı alanlarında
yoğunlaşmaktadır (Zhang vd., 2013). Kıyı
bölgelerinde artan nüfusla birlikte, kıyı değişiminin
incelenmesi araştırmacıların en önem verdiği
konulardan biridir (Moore, 2000). Kıyı çizgisinde
meydana gelen değişimlerin hızlı ve doğru bir
şekilde belirlenmesi sadece kıyı ıslahı, kentsel
büyüme ve liman geliştirme faaliyetleri için değil
aynı zamanda denizcilik ekonomisi ve denizcilik
araştırmaları için de önemli bir konudur (Zhang vd.,
2013).
Kıyı çizgisini çıkartmak için fotogrametrik
yöntemler, GPS teknolojisi ve yersel ölçüler, uzaktan
algılama gibi çeşitli yöntemler kullanılmaktadır
(Zhang vd., 2013). LANDSAT uydusunun 1972'de
kullanılmaya başlanılmasından bu yana optik
uzaktan algılama verileri diğer yöntemlerden elde
edilen verilere bir alternatif haline gelmiştir (Gens,
2010). Kontrolsüz sınıflandırma teknikleri
(ISODATA-Iterative Self Organized Data Analysis)
bant oranlama, normalize edilmiş fark su indeksi
(NDWI) eşik değer ve morfolojik filtreleme, Wavelet
dönüşümü, aktif kontur modelleri (Zhang vd., 2013),
nesne tabanlı, genetik algoritma, kontrollü ve
kontrolsüz sınıflandırma, parçacık sürü
optimizayonu (PSO), Mean-shift bölütleme
(İncekara vd., 2018) optik uydu görüntülerinden kıyı
çizgisi çıkarmak için kullanılan yöntemlere örnek
olarak verilebilir. Son yıllarda makine öğrenmesi
yöntemleri uzaktan algılama problemlerinde yaygın
olarak uygulanmaktadır (Lary vd., 2016). Çeşitli
çalışmalarda kıyı çizgisi çıkarımında makine
öğrenmesi yöntemleri kullanılmıştır (Dixon &
Candade, 2008; Kalkan vd., 2013; Bayram vd., 2017).
Choung & Jo, 2017 Worldview-2 uydu görüntüleriyle
bir makine öğrenmesi yöntemi olan Destek Vektör
Makineleri (Support Vector Machines) ile adaptif
eşikleme ve NDWI yöntemin kıyı çizgisi
çıkarımındaki performansını araştırmıştır.
Derin öğrenme (DL), Goodfellow vd., 2016
tarafından bilgisayarların dünyayı kavram
hiyerarşileri açısından anlamasını ve insanlara
benzer şekilde karar vermesini sağlayan makine
öğrenmesi olarak tanımlanmaktadır. Klasik makine
öğrenmesinde özellik çıkartma işlemi kullanıcı
tarafından yapılmaktadır ve bu zaman alıcı ve
kullanıcı odaklı bir süreçtir. Derin öğrenme
yaklaşımında ise özellik çıkartma işlemi otomatik
olarak yapılmaktadır (Patterson & Gibson, 2017).
DL yöntemleri, son yıllarda kıyı alanlarına
yönelik çalışmalarda yaygın olarak kullanılmaya
başlanmıştır. Yang vd., 2015 LANDSAT uydu
görüntülerinde SSAE (Stacked Sparse Autoencoder)
derin öğrenme mimarisini kullanarak kara-su
bölütlemesi gerçekleştirmişlerdir. Yu vd., 2017
LANDSAT-7 görüntülerinden kıyı çizgilerini
çıkarmak için evrişimsel sinir ağları ve lojistik
regresyon sınıflandırıcısından oluşan karma bir
makine öğrenimi sistemi sunmuştur. Işıkdoğan vd.,
2017 DeepWaterMap adlı kodlayıcı-kod çözücü
derin öğrenme mimarisine dayalı Tam
Konvolüsyonlu Ağ (FCNN) yapısı kullanarak
LANDSAT-7 uydu görüntülerinde kara-su
bölütlemesi gerçekleştirmişlerdir. Li vd., 2018 kıyı
çizgisi bölütlemesi için DeepUNet adlı genişleyen
konvolüsyonel sinir ağları tabanlı bir yaklaşım
önermiştir. Chen vd., 2018 süper piksel ve
konvolüsyonel sinir ağı algoritmalarını kullanarak
yüksek çözünürlüklü çok bantlı görüntülerden kıyı
çizgisi çıkarmıştır. Song vd., 2020 Worldview-3 ve
GeoFen-2 görüntülerinden Mask R-CNN yöntemini
kullanarak su sınıfını yüksek doğruluklar ile
üretmişlerdir. Erdem vd., 2020 tarafından yapılan
çalışmada LANDSAT-8 görüntülerinden su sınıfının
çıkarılması için WaterNet adında 5 farklı U-Net derin
öğrenme modelinin kombinasyonu kullanan bir
yöntem geliştirilmiştir.
Uzaktan Algılama çalışmalarında derin öğrenme
modellerinin uygulanmasında aktarımlı öğrenme
(transfer learning) yaygın olarak kullanılan bir
yöntemdir. Aktarımlı öğrenme ile bir veri seti için
yapılan eğitim işlemi sonucunda oluşturulan ağırlık
parametresi, bir başka veri setinin eğitilmesi için
başlangıç ağırlıkları olarak kullanılır. Bu durum, az
sayıda veri ile yüksek doğrulukta sonuçlar üretmek
açısından avantajlar sağlamaktadır (Torrey &
Shavlik, 2009).
Yapılan literatür araştırmasında SENTINEL-2
görüntülerinden aktarımlı öğrenme yöntemi
kullanılarak kara-deniz bölütlemesi ve kıyı çizgisi
çıkartmaya yönelik bir çalışmaya rastlanmamıştır.
Bu çalışmada, önceden LANDSAT-8 uydu görüntüleri
ile eğitilmiş U-Net mimarisi (Erdem, vd., 2020) ve az
sayıda SENTINEL-2 uydu görüntüsü veri seti
kullanılarak aktarımlı öğrenme ile kıyı çizgisi
çıkarılmıştır.
2. YÖNTEM
Bu çalışmada SENTINEL-2 veri setinden karadeniz bölütlerinin U-Net mimarisi ile elde edilmesi
için YTU-WaterNet açık veri seti (URL-1) ile eğitilen
U-Net mimarisinin ağırlıkları (Erdem, vd., 2020)
başlangıç ağırlıkları olarak kullanılmıştır.
2.1. Veri
Sunulan çalışmada, aktarımlı öğrenme için
farklı kıyı bölgelerinden alınan 10m konumsal
çözünürlüğe ve 15-bit radyometrik çözünürlüğe ve
mavi, kırmızı ve yakın kızılötesi bant
kombinasyonuna sahip toplam 15 adet SENTINEL-2
uydu görüntüsü kullanılarak eğitim ve test veri