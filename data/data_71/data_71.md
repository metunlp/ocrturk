Bu tipteki sinir ağlarına daha fazla sayıda gizli katman (ikiden fazla) eklenmesiyle doğrusal
olmayan karmaşık ilişkilerin de tespit edilebilmesi sağlanmıştır ve elde edilen bu sinir ağlarına
derin sinir ağları (DSA) adı verilmiştir. DSA’lar hem (işaretli veriler varsa) denetimli, hem de
kümeleme gibi denetimsiz öğrenme problemleri için kullanılabilmektedir. DSA’lar yaygın olarak
sınıflandırma ve regresyon amacıyla kullanılmakta ve başarılı sonuçlar elde edilmesini
sağlamaktadırlar. Ancak öğrenme süreçleri oldukça yavaş olabilmektedir (Ravì vd., 2017).
2.2. Derin Oto-Kodlayıcılar
Oto-kodlayıcılar, problem çözümü için gerekli öznitelik kümesinin veriden otomatik olarak
çıkarılması amacıyla ortaya atılmış sinir ağlarıdır. Bir oto-kodlayıcı, girdi vektörüne bir sınıf etiketi
vermek yerine onu yeniden oluşturmak için öğretilmektedir (Ravì vd., 2017).
Derin öğrenmenin konusu olan derin oto-kodlayıcılar ise, çok boyutlu veriyi temsil etmek için
birden fazla oto-kodlayıcının birbiri üstüne kümelenmesiyle oluşan mimarilerdir (Hinton ve
Salakhutdinov, 2006). Literatürde, derin oto-kodlayıcıların birçok farklı türü önerilmiştir.
Derin oto-kodlayıcıların amacı, öznitelik kümesini otomatik çıkarmak veya veri boyutu
sayısını azaltmaktır (Hinton ve Salakhutdinov, 2006). Bu yöntemde öğrenme için işaretli veri
kümesine ihtiyaç yoktur, yani denetimsiz bir öğrenme yöntemidir. Ancak yöntem uygun ağırlıkları
bulabilmek için bir ön-öğrenme aşamasına ihtiyaç duymaktadır. Bu ön-öğrenme aşamasında son
konfigürasyona uygun yaklaşık ağırlıklar yönteme sağlanmaktadır (Ravì vd., 2017).
2.3. Derin Ġnanç Ağları
Derin inanç ağları (Hinton vd., 2006) ve bir sonraki bölümde tanıtılacak olan derin Boltzmann
makineleri, sınırlandırılmış Boltzmann makinesi adı verilen bir algoritmaya (Hinton ve Sejnowski,
1986) dayanmaktadır. SBM algoritması stokastik bir sinir ağı olarak tanımlanmakta ve bu ağlarda
Gaussian gibi belirli bir dağılıma sahip stokastik birimler kullanılmaktadır. Öğrenme sürecinde ise
Gibbs örneklemesi gibi ağırlıkları adım adım ayarlayan yöntemler kullanılmaktadır.
Derin inanç ağları birden fazla SBM’nin bileşkesi olarak algılanabilir (Hinton vd., 2006). Her
bir SBM’nin gizli katmanı, bir sonraki SBM’nin görünür katmanına bağlanmıştır ve en üst seviyede
yönsüz bağlantılar vardır. Derin inanç ağları hem denetimli hem de denetimsiz öğrenme amacıyla
kullanılabilir. Bu ağı başlatmak için katman-katman bir açgözlü algoritma ile öğrenme
gerçekleştirilmektedir (Ravì vd., 2017).
2.4. Derin Boltzmann Makinesi
Boltzmann makinelerine dayalı bir diğer derin öğrenme yöntemi de derin Boltzmann
makineleridir (Salakhutdinov ve Larochelle, 2010). Derin inanç ağlarından farkı; derin Boltzmann
makinelerinde ağın tüm katmanları arasında yönsüz bağlantıların olmasıdır. Bir diğer fark ise derin
Boltzmann makinelerinde zaman karmaşıklığının daha fazla olması bu nedenle de büyük veri
kümelerinde öğrenme sürecinin yavaş olmasıdır (Ravì vd., 2017).
2.5. Yinelenen Sinir Ağları
Yinelenen sinir ağları (Williams ve Zipser, 1989), veri akışlarını (stream of data) analiz
edebilen gizli katmanlara sahip sinir ağlarıdır ve çıktının bir önceki hesaplamalara bağlı olduğu
problemlerin çözümü için çok uygundur (Ravì vd., 2017). Yinelenen sinir ağları bu nedenle
özellikle doğal dil işlemenin değişik problemlerinin çözümünde oldukça başarılı olmuştur (Ravì
vd., 2017). Yinelenen sinir ağlarında öğrenme sırasında ortaya çıkan bazı problemler nedeniyle, bu
ağların uzun kısa-dönem bellek (Long Short-Term Memory - LSTM) (Hochreiter ve Schmidhuber,
1997) gibi farklı sürümleri literatüre girmiştir.