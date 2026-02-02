are used for the prediction of power outputs obtained from PV panels monthly. Particle Swarm Optimization (PSO), Back-
Propagation (BP), Clonal Selection Algorithm (CSA) are used to train ANN to predict six different PV panel located in different
angles from 10 to 60 degrees. Three different popular evaluation methods which are called mean absolute percentage error (MAPE),
root mean square error (RMSE), varyans (R2) used to do comparison. According to examination of verification results, PSO is almost
most successful algorithm as a training method when it is compared with BP and CSA. It is seen for the some of the results belong to
a few months that BP is slightly better than PSO.

Keywords: Photovoltaic Panel, Power Prediction, ANN, Back-propagation; PSO, Clonal Selection Algorithm

1\. Giriş

Dünyada ve onun küçük bir yansıması olarak Türkiye’de; gelişen teknoloji beraberinde aynı oranda artan bir enerji ihtiyacını
ortaya çıkarmaktadır. Bu ihtiyacın giderilmesi için kullanılan kaynaklar incelendiğinde, bölgesel olarak farklılıklar olsa da fosil yakıt
türlerinin ön plana çıktığı görülmektedir. Türkiye’ye ait yıllık istatistikler incelendiğinde enerji ihtiyacının %66.7’si fosil yakıtlardan,
%25.3’ü hidrolikten, %8.1‘i ise jeo-termal, rüzgar, güneş enerjisi ve diğer kaynaklardan elde edilmektedir[1,2]. Gelişen ihtiyaçlara
cevap verebilmek adına devletler mevcut politikalarını gözden geçirerek, gerek tükenme olasılığı, gerekse çevreye etkileri
düşünülerek fosil yakıtlara alternatif olan enerji kaynaklarını ve üretim yöntemlerini araştırmaya başlamışlardır.

Elektrik enerjisi elde etmek için kullanılan yöntemlerden birisi de FV paneller yardımıyla güneş enerjisinden yararlanmaktır.
Özellikle güneş enerjisi, diğer enerji kaynaklarına göre temiz, sessiz, ekonomik, güvenilir ve tükenmez olması nedeniyle son
zamanlarda daha da önemli hale gelmiştir [3]. FV panellerden üretilen enerji, coğrafi konum, mevsimsel değişimler ve çevresel
koşullar gibi faktörlere göre değişiklikler gösterebilmektedir. Buna bağlı olarak FV panellerin eğim açısının aylık, mevsimsel ve yıllık
olarak değiştirilmesi ile panellerden en yüksek gücün elde edilmesi sağlanabilmektedir. Güncel ve modern güç sistemlerinin güvenli
ve ekonomik olarak işletilmesi için üretim planlamaları gerçek zamanlı, günlük, haftalık, aylık ve yıllık olarak yapılabilmektedir.
Bundan dolayı, FV panel istasyonları gibi yenilenebilir güç tesislerinin güç çıkış değerlerinin ve yük eğilimlerinin kestirilmesi temel
bir süreç olarak ortaya çıkmaktadır.

Solar güç istasyonlarının verimliliğinin(çıkış gücü), farklı hava koşullarına göre değişimler gösterdiği bilinen bir gerçektir. Bu
nedenden dolayı, son zamanlarda FV panellerin güç çıkış değerlerinin tahmin edilmesine yönelik çalışmaların önemli ölçüde arttığı
görülmektedir. Günümüzde FV panellerin güç tahmini için yaygın olarak kullanılan iki temel yaklaşım bulunmaktadır [4]. Bunlardan
birincisi, solar ışınım, ortam sıcaklığı ve matematiksel modelleri kullanılarak elde edilen bazı parametreler gibi çevresel
parametrelerin tahmini yardımıyla FV sistemlerindeki aktif gücün hesaplanmasıdır. Diğeri ise, FV sistemlerin aktif güç çıkışlarının
doğrudan tahmin edilmesidir [5]. Solar ışınım verilerinin saatlik olarak tahmin edilmesi çok zor olduğundan dolayı, Kudo vd.[5]’ un
çalışmasında aktif güç çıkışı, daha önce ölçülen akım ve gerilim verilerine bağlı olarak doğrudan tahmin edilmiştir.

Literatürde, şimdiye kadar FV panel güç çıkışlarının tahmini için birçok yöntem önerilmiştir. Lorenz vd. [4] ve Kudo vd. [5] hava
durumu verileri kullanarak FV panel güç çıkış karakteristiklerini ortaya koyan, çoklu doğrusal regresyon yöntemleri ve YSA
modelleri kullanılarak elde edilen solar ışınım tahminlerini karşılaştırmalı birer çalışma ile sunmuşlardır. Junseok vd. [6] ve Li vd. [7],
Markov zincirleri kullanarak olasılıksal bir yaklaşım ile Fotovoltaik üretim merkezlerinde enerji depolama birimleri üzerine çalışma
yapmışlardır. Ran vd. [8] ve Shi vd. [9] ise çalışmalarında, bir makine öğrenmesi yöntemi olan Destek Vektör Makineleri ile FV panel
güç çıkışlarının tahmin edilmesine yönelik çalışmalar yürütmüşlerdir. Wang [10] çalışmasında, yukarıdaki çalışmaların dışında, FV
güç çıkışlarının tahmin edilmesinde en uygun metodun YSA olduğu bazı çalışmalarda ortaya koymuştur. Kou vd. [11] çalışmalarında,
GY kullanarak eğitilen YSA yapısı ile meteoroloji verilerinin de kullanılması sayesinde solar panel çıkış gücü tahmini yapmışlardır.
Zhang vd. [12], PSO evrimsel algoritmasını hibrit bir yöntem haline getirerek yapay sinir ağını eğittikleri çalışmalarında, ışınım
değerlerini de girdi olarak kullanmış ve solar radyasyon tahmin çıkarımları elde etmişlerdir. Qasrawi [13], farklı bölgelere
yerleştirilen güneş panellerinden alınan panel çıktıları ve uydulardan alınan veriler ile birlikte çok katmanlı ve GY (Levenberg-
Marquardt) ile eğitilmiş YSA tasarlamışlardır. Sisteme girdi olarak nem, solar ışınım, gün ışı süresi uzunluğu, bulutsuz hava şartları
verilmiştir. Test verileri ile ağın başarımı doğrulanmıştır. Zhu vd. [14], dalgacık dönüşümü(wavelet transform) yöntemi ile verilere
indirgeme uygulamışlardır. Bu verileri YSA’nın eğitiminde kullandıkları hibrit bir yöntem çalışmasının ardından tekrar dalgacık
ayrıştırması Yöntemi ile veriyi yapılandırma işlemine tabi tutmuşlar ve mevcut YSA çalışmalarına oranla daha az matematiksel işlem
gerektiren bir çalışma ortaya çıkarmışlardır. Prokop vd. [15], ANFIS ve çok katmanlı algılayıcı (MLP) yöntemler ile bir çalışma
önermişlerdir. ANFIS ve MLP’nin benzer davranışlar sergileyerek ortalama %2’lik bir kesinlikte tutarlı sonuçlar elde etmişlerdir.
ANFIS’in MLP’ye nazaran daha kesin sonuçlar verdiklerini çalışmalarında belirtmişlerdir. Paulin ve Praynlin [16], güneş panellerinde
ortalama ortam ısısı, ortalama panel ısısı, dönüştürücü ortalama ısısı, solar ışınım, rüzgar hızı ve güç çıkışı verilerini girdi olarak
kullanarak GY tabanlı YSA’yı eğittikleri karşılaştırmalı bir çalışma ortaya koymuşlardır. Rana vd. [17], farklı YSA yapılarından
oluşan bir iteratif ve iteratif olmayan iki farklı yöntemin vermiş olduğu sonuçları karşılaştırarak iteratif olan yöntemin diğerlerine göre
yakın sonuçlar verdiğini göstermişlerdir.

Bu çalışmada ise geriye yayılım gibi klasik algoritmalardan farklı olarak sezgisel yöntemler kullanılarak eğitilen bir YSA modeli
ile farklı eğim açılarına (100,200, 300, 400, 500, 600) yerleştirilmiş FV panel güç çıkışlarının, akım ve gerilim değerlerine bağlı bir
şekilde aylık olarak tahmin edilmesine yönelik hibrit bir yöntem önerilmiştir. Önerilen bu çalışmada, geriye yayılım algoritması
yardımıyla elde edilen güç değerleri ile sezgisel yöntemler olan PSO ve KSA sezgisel algoritmaları ile elde edilen güç değerlerinin
karşılaştırılmalı değerlendirmesi de yapılmıştır. Ayrıca, yöntemin elde edilen sonuçlar üzerindeki etkinliği ölçüm yapılan gerçek ve
tahmin edilen değerler arasındaki ortalama yüzdelik hatanın analizi ile doğrulanmıştır. Çalışmanın sonraki aşamaları şu şekilde
organize edilmiştir. İkinci bölümde deneysel düzenek ve veriseti ile kullanılan algoritmalar çalışmanın materyal ve metot kısmı olarak