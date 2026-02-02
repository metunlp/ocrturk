seyrek görünüme dayalı öğrenme yaklaşımının mevcut son teknoloji yaklaşımlarını önemli ölçüde geride bıraktığını ve manuel kadar
sağlam olduğunu göstermiştir.

Nie ve ark. glioma adı verilen beyin tümörünün erken teşhisi için yaptıkları çalışmada yüksek dereceli glioma hastalarının
ameliyat öncesindeki çok modlu beyin görüntülerinden otomatik özellik çıkarımı yapabilmek için derin öğrenme yöntemini
kullanmışlardır. Özellikle, 3 boyutlu ESA’yı benimsemiş ve çok kanallı veri ve danışmanlı özellik öğrenme ile yeni bir ağ mimarisi
önermişlerdir. Klinik özelliklere odaklı, hastanın sağ kalım süresini öngörmek için destekli vektör makinesinde eğitim yapılmıştır.
Kullandıkları yöntem % 89,9 doğruluk değeri elde etmiştir. Çok modlu beyin görüntülerinden öğrenilen özelliklerin doğru zaman
tahmininde önemli bir rolü olduğunu ortaya koymuşlardır [58].

Kleesiek ve ark.[59] derin MRG görüntülerinden beyin çıkarımı yapmaya çalışmışlardır. Kafatası sıyırma için 3 boyutlu ESA
kullanmışlardır. İkili maskeleri üretmek için kesme eşiğinin ESA’nın olasılık çıktısından üretilmesinin, yöntemin hassasiyetini
arttırmak için kullanılabileceğini ifade etmişlerdir. Ancak bunun özgüllüğün azalmasına sebep olabileceğini ve uygulamaya özel
olarak karar verilmesi gerektiğini vurgulamışlardır. Optimize edilmiş bir GPU uygulaması kullanarak tahminlerin bir dakikadan daha
kısa sürede gerçekleştirilebileceğini ve önerilen yöntemin, büyük ölçekli çalışmalar ve klinik denemeler için faydalı olabileceğini
söylemişlerdir.

Jiang ve ark. görüntülerde ön işleme yapabilen ve somatik hücre kaynağındaki sinir öncü ve sinir öncü olmayan hücreleri
sınıflandırabilen ESA temelli yeni bir tanıma sistemi önermişlerdir. Puleripotent kök hücreleri, sınırsız çoğalma yeteneğine sahip,
embriyonik kök hücre olarak da bilinen bütün organ ve dokulara dönüşebilen rejeneratif tıp için önemli olan, gelişen embriyoda
ektoderm hücreleri tarafından oluşturulan iç hücre kitlesidir. Elde ettikleri deneysel sonuçlar ile önerdikleri sistemin uyarılmış
puleripotent kök hücreleri ve sinir öncü hücrelerinden ilaç üretilmesi ile ilgili araştırmalarda kullanılabilecek yeni bir araç sağladığını kanıtlamışlardır [60].

Havaei ve ark. MRG görüntülerinden fokal beyin patolojisi segmentasyonu için GPU destekli ESA uygulamasını medikal
görüntülemede kullanmışlardır [61]. Yöntemleri başarılı sonuçlar elde etmiştir. Oluşturulan ESA modelinde İlk satırda, iki yollu ESA
bulunmaktadır. Girdi yaması, her biri yerel bir ağdan oluşan iki ağ ve global bir yol üzerinden geçmektedir. Yerel ve küresel
yollardaki özellik haritaları sarı ve turuncu renkte gösterilmektedir. İkinci satırda art arda girdili ESA bulunmaktadır. Sınıf olasılıkları iki yollu ESA tarafından üretilen ikinci bir ESA modelinin girdisi ile birleştirilmektedir. Üçüncü satırda, kademeli girdili ESA kullanılarak tam görüntü tahmini yapılmaktadır.

Suk ve ark. [62] Derin öğrenme yoluyla nöro görüntüleme yöntemlerinden üst düzey gizli ve paylaşılan özellik gösterimi için
yeni bir yöntem önermişlerdir. Özellikle, 3 boyutlu bir yamayla gizlenmiş hiyerarşik özellik gösterimini bulmak için bir yapı bloğu
olarak KBM’ye sahip derin bir ağ olan Derin Boltzmann Makinesini (DBM) kullanmışlardır. Çok modelli bir DBM ile eşleştirilmiş
MRG ve PET (Pozitron emisyon tomografisi) yamalarından ortak özellik gösterimi için sistematik bir yöntem geliştirmişlerdir.
Önerilen yöntemin etkinliğini doğrulamak için, ADNI (Alzheimer Hastalığı Nöro Görüntüleme Girişimi) veri kümesi üzerinde
deneyler yapmışlar ve elde ettikleri sonuçları son teknoloji yöntemlerle karşılaştırmışlardır. AD (Alzheimer hastası) ve sağlıklı
(Normal Kontrol) NC, MCI (Hafif bilişsel bozukluk) ve NC, MCI dönüştürücü ile MCI dönüştürücü olmayan üç ikili sınıflandırma
problem üzerinde çalışmışlardır. Eğitimli modelin görsel incelemede diğer yöntemlerden daha iyi performans gösterdiğini ve
sırasıyla% 95,35, % 85,67 ve % 74,58 oranlarında maksimum doğruluk değerini elde ettiğini ifade etmişlerdir.

Kuang ve He [63] dikkat eksikliği hiperaktivite bozukluğunu (ADHD) araştırmışlardır. Kamuya açık veri setinde ADHD
verilerinin özelliklerine göre yapıyı ve parametreleri ayırt etmek için derin öğrenme modellerinden biri olan DSA ’i özellik ve
sınıflandırma için kullanmıştır. Denekleri kontrol, kombine, dikkatsiz veya hiperaktif gibi frekans özelliklerine göre tahmin
etmişlerdir. Sonuçlar, diğer yöntemler ile karşılaştırıldığında büyük ölçüde iyileşme sağlamıştır. Uyguladıkları derin öğrenme
yönteminin ADHD ’nin (Fonksiyonel manyetik rezonans görüntüleme) fMRG verileri ile ayırt edilmesinde ilk kez kullanıldığını iddia
etmişlerdir.

Li ve ark. Alzheimer hastaları ile hafif bilişsel bozukluk hastalarının teşhisi için yaptıkları çalışmada dayanıklı ya da sağlam
olarak ifade edilen Derin Öğrenme yöntemini geliştirmişlerdir. Uyguladıkları yöntem diğer derin öğrenme metotlarına göre % 5.9
oranında doğruluk sınıflandırmasında daha iyi sonuç vermiştir [64].
Fritscher ve ark. [65] çalışmalarında, 3 boyutlu tıbbi görüntülerin hızlı segmentasyonu için ESA kullanmışlardır. ESA modelinde
girdi olarak görüntü yamalarının kullanmalarının yanı sıra, şekil ve konum bilgisini ESA eğitimi için yoğunluk bilgisi ile birleştiren
ortogonal yamalar da kullanmışlardır. Bu amaçla, baş-boyun bölgesi için BT (Bilgisayarlı Tomografi) veri kümesi kullanılmış ve
sonuçları diğer atlas ve model tabanlı yaklaşımlar ile karşılaştırmışlardır. Sunulan yaklaşımın tamamen otomatik ve hızlı olduğunu,
bununla birlikte belirli anatomik yapılarla sınırlı olmadığını öne sürmüşlerdir. Yaptıkları nicel değerlendirmenin iyi sonuçlar verdiğini ve tıbbi görüntülerin bölümlendirilmesinde derin öğrenme yaklaşımları için büyük potansiyel olduğunu söylemişlerdir.

Zhen ve ark. [66] çift ventrikül hacim tahmini için DİA mimarisini kullanmışlardır. Büyük ölçekli derin ağlar tarafından
denetimsiz kardiyak görüntü temsili öğrenme ve rastgele ormanlar tarafından doğrudan çift ventrikül hacim tahmini olarak iki ana tam
öğrenme aşamasından oluşan genel bir regresyon çerçevesi tanımlamışlardır. Üretken ve ayırt edici öğrenmenin güçlü yanlarından
faydalanan önerdikleri yöntemin, daha önceki yöntemlerde kullanılan hastaların iki katı olan hem sağlıklı hem de hastalıklı vakaları
içeren 100 denekten oluşan daha geniş bir veri setinde, uzmanlar tarafından hem sol hem de sağ ventrikül için toprak dışına çıkma
çapraz onaylama yöntemiyle karşılaştırıldığında yaklaşık 0,92’lik yüksek korelasyonlar ürettiğini ve büyük ölçüde mevcut doğrudan
yöntemlerden daha iyi performans gösterdiğini söylemişlerdir. Bununla birlikte önerdikleri yöntemin, klinik kardiyak fonksiyon
analizinde pratik olarak kullanımının yanında, diğer organ hacmi kestirim görevlerine kolayca genişletilebileceğini iddia etmişlerdir.