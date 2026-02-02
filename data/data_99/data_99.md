yıllarda daha çok makine öğrenmesi temelli çalışmalar yapmışlardır. Albuquerque ve diğerleri (2022) her iki
yaklaşımı değerlendirmiş ve geleneksel yöntemlerin tahmin için uygun olmadığını, öte yandan, makine öğrenmesi
modellerinin, eğitim için kullanılan kullanıcı tanımlı hiper-parametrelerdeki küçük değişikliklere bile son derece
duyarlı olduğu için oldukça farklı sonuçlara yol açabileceğini ve modelin genel tahmin performansını
etkileyebileceğini belirtmişlerdir.
Finansal varlıkların fiyat hareketleri doğrusal olmayan çok değişkenli bir yapıya sahip oldukları için makine
öğrenmesi yöntemleri, algoritmik ticaret, yatırım yönetimi, servet yönetimi ve risk yönetiminde geleneksel
yöntemlere göre daha iyi sonuçlar vermektedir (Dixon ve diğerleri, 2020). Bununla birlikte, geleneksel makine
öğrenmesi yöntemlerinde model başarımı kullanılan özniteliklere bağlıdır. Finansal zaman serisi verileri için
uygun öznitelikleri belirlemek ise, neredeyse imkânsız bir görevdir. Ancak öznitelik çıkarımını ağ katmanları
boyunca kendiliğinden gerçekleştiren derin öğrenme tekniklerinin kullanılması sayesinde bu zorlu görevi
başarmak daha mümkün hale gelmiştir. Bu sebeple, finansal zaman serisi tahmini için derin öğrenme tabanlı
çalışmalar öne çıkmaya başlamış ve son yıllarda artan bir ilgiyle devam etmektedir.
Derin öğrenme tabanlı finansal zaman serisi tahmini konusunda yayınlanmış derleme makaleler, en çok
kullanılan derin öğrenme modelinin Özyineli Sinir Ağları (RNN) ve bir varyasyonu olan Uzun Kısa Süreli Bellek
Ağları (LSTM) olduğunu ortaya koymaktadır (Durairaj ve Mohan, 2019; Li ve Bastos, 2020; Ozbayoglu ve
diğerleri, 2020; Sezer ve diğerleri, 2020). Moghar ve Hamiche (2020), gelecekteki borsa değerlerini tahmin etmek
için RNN ve LSTM kullanarak bir model oluşturmayı amaçlamışlardır. Yazarlar yaptıkları çalışmada 19/08/2004
ile 19/12/2019 tarihleri arasındaki NKE ve GOOGL hisselerine ait fiyat değişim verileri üzerinde çalışarak
önerdikleri yöntemle klasik metotlara göre daha başarılı sonuçlar elde edildiğini ortaya koymuşlardır. Bukhari ve
diğerleri (2020) finansal piyasa tahmini için Otoregresif Kesirli Entegre Hareketli Ortalama (ARFIMA) ve LSTM
modellerinin bir kombinasyonuna dayanan hibrit ARFIMA-LSTM modelini önermişlerdir. Bu hibrit model, piyasa
değişkenleri yardımıyla veriden potansiyel bilgileri çıkarır ve her iki modelin öneri kümesinin kesişimini alarak
tahmin doğruluğu açısından daha iyi performans elde eder. Yoo ve diğerleri (2021) piyasa verilerindeki değişim
noktalarını tahmin etmek için Gürültü Giderici Otomatik Kodlayıcı (DAE) ve LSTM modelini kullanmışlardır.
Yazarlar, çeşitli sektörlerdeki piyasa verilerini ampirik olarak ele almış, DAE kullanarak veriyi önemsiz
özniteliklerden arındırmış ve bu veriyi LSTM modeli ile eğitmişlerdir. Elde ettikleri sonuçlar genel olarak dikkat
çekicidir. Bhandari ve diğerleri (2022) S&P 500 endeksinin ertesi gün kapanış fiyatını tahmin etmek için tek
katmanlı ve çok katmanlı LSTM modellerini karşılaştırmışlardır. Bu karşılaştırma sonunda tek katmanlı
modellerin tahmin yeteneğinin daha üstün olduğunu tespit etmişlerdir.
Bilgisayarlı görü problemlerinin çözümünde üstün performans göstermesi nedeniyle Evrişimsel Sinir Ağları
(CNN) en çok kullanılan derin öğrenme modellerinden biridir. CNN modellerinin bilgisayarlı görü
çalışmalarındaki üstün performansı doğal dil işleme ve zaman serisi analizi gibi farklı alanlardan araştırmacıların
da dikkatini çekmiş ve kendi problemlerine adapte etmişlerdir (Fawaz ve diğerleri, 2019). Finansal zaman serisi
tahmini çalışmalarında CNN modelleri tek başlarına ya da hibrit modellerde çözümün bir parçası olarak
kullanılmışlardır. Ve bu alandaki kullanımları artan bir ilgiyle devam etmektedir. Ozbayoglu ve diğerleri (2020)
finansal zaman serisi tahmininde derin öğrenme kullanımını inceledikleri derleme çalışmalarında, finansal zaman
serisi verilerinin görüntü temsillerinin CNN ile modellenmesinin yenilikçi bir alan olduğunu belirtmişlerdir.
Khodaee ve diğerleri (2022) hisse senedi dönüm noktalarının tahmin edilmesi için LSTM ve CNN modellerini
birleştiren hibrit bir yöntem önermişlerdir. Yazarlar bu hibrit modeli ResNet ağında eğiterek daha güçlü hale
getirmiş ve Dow-30'da ortalama %60,19 ve ETF'lerde %63,62'lik ortalama doğru tahmin başarısı göstermişlerdir.
Mehtab ve Sen (2022), CNN ve LSTM tabanlı derin öğrenme modeli oluşturarak bu modeli piyasa verileri üzerinde
test etmiş ve yürütme süresi, ortalama hata gibi metriklerle performans sonuçlarını sunmuşlardır. Kirişçi ve Yolcu
(2022) finansal zaman serisi tahminine yönelik olarak CNN tabanlı model önererek bu modeli TAIEX ve FTSE
borsalarının verileriyle eğitmişlerdir. Yazarlar, CNN yapısının, farklı yapay sinir ağı türleri, LSTM, bulanık tabanlı
yaklaşımlar ve bazı geleneksel yöntemlere göre daha başarılı olduğunu belirtmişlerdir. Gong ve diğerleri (2022)
AAPL hisse senedi üzerinde teknik analiz göstergelerini temel alan üç katmanlı bir tahmin modeli oluşturmak için
CNN kullanmıştır. Bu üç katman; (i) öz nitelikleri çıkaran evrişim katmanı, (ii) doğrultulmuş lineer birimler
(ReLU) katmanı ve (iii) toplu normalleştirme katmanıdır. Durairaj ve Mohan (2022), kaos teorisi, CNN ve polinom
regresyon içeren hibrit bir yaklaşımla finansal zaman serisi tahmini yapmışlardır. Altuntaş ve diğerleri (2022) ons
altın fiyat verilerini mum grafikleri ve teknik analiz göstergeleri kullanarak grafik görüntülere dönüştürdüler.
Alım-satım sinyalleri üretmek için ön-eğitimli CNN mimarisini ince-ayarlayarak fiyat yön tahmini için kullandılar.
Önerdikleri modelin %53,8 doğruluk ve 3 yıllık test dönemi için %48,42 kâr ile karşılaştırılan diğer yatırım
stratejilerinden daha başarılı sonuçlar ürettiğini bildirdiler.
Endeksler borsada işlem hacmi ve değer olarak en büyük şirketlerin performansını gösteren bir ölçektir. Borsa
İstanbul’un performansı BIST100 endeksi ile ölçülür. Bu nedenle, borsa yatırımcıları tarafından borsanın genel
durumunu anlamak için kullanılır. Borsa yatırımcıları kendi portföylerindeki hisse senetleri için alım-satım kararı
verirken BIST100 endeksinden yararlanırlar. Her ne kadar endeksler birer finansal enstrüman olmasalar da portföy 