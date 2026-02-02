hale getirebilmek adına gizli katman(lar)a iletir. Gizli katman(lar)da gerçekleştirilen çeşitli
işlemler sonucunda elde edilen veriler dış dünyaya aktarılmak üzere çıkış katmanına iletilir. Basit
problemler için temelde bir ya da iki adet gizli katman oluşturmak sonuca ulaşmak için yeterli
olurken daha karmaşık problemleri anlayabilmek, örüntüleri tanımak ve çeşitli ilişkiler
çıkarabilmek için onlarca hatta yüzlerce gizli katman kullanmak gerekebilir.

Derin öğrenme, çok katmanlı yapay sinir ağlarını kullanan ve doğal dil işleme alanında en sık
kullanımına rastlanılan makine öğrenmesi türlerinden biridir. Gerçek dünya problemlerinin
çözümü için insan benzeri performans göstermeye oldukça yakın bir makine öğrenmesi türüdür.
İstatistiksel yöntemler ve geleneksel makine öğrenmesi yöntemlerinden farklı olarak belirli
kurallar kullanarak öğrenmek yerine elde bulunan veriden, verinin büyüklüğüne paralel olarak
artan bir başarı oranı ile karmaşık özellikleri otomatik olarak öğrenmektedir. Her katmandaki bilgi
önceki katmanlardaki bilgilerden hesaplama yoluyla temsil edilerek verilerdeki karmaşık yapılar
keşfedilmeye çalışılır. Yapay sinir ağları kullanılarak birçok derin öğrenme türü geliştirilmiştir.
Doğal dil işleme alanında sıklıkla karşılaşılan derin öğrenme yöntemlerine Üretken Çekişmeli
Ağlar (Generative Adversarial Networks, GAN), Tekrarlayan Sinir Ağları (Recurrent Neural
Network, RNN), Uzun Kısa Süreli Bellek (Long Short Term Memory, LSTM), Geçitli Yinelenen
Birim (Gated Recurrent Unit, GRU), Transformer mimarisi örnek verilebilir.

3. ARAŞTIRMA METODU
Bu bölümde, gerçekleştirilen çalışma kapsamında incelenen literatürdeki makaleleri belirleme
kriterleri açıklanmaktadır. Literatür araştırması için Google Akademik arama motoru tercih
edilmiştir. Aramalar gerçekleştirilirken “code generation”, “generating programming language
code from natural language”, “generating code from natural language” gibi aynı anlama gelen
farklı anahtar kelimeler kullanılarak makaleler taranmıştır. Çalışmalar 2000 ila 2022 yılları
arasında sınırlandırılmıştır. Taranan makaleler arasından belirlenen çalışmalar, bulundukları veri
tabanlarında detaylı bir şekilde incelenmiştir. Aramalar gerçekleştirilirken makale türü, makale
dili, herhangi bir doğal dil veya hedeflenen programlama dili için özel ölçüt belirlenmemiştir.
Literatür araştırması için seçilen çalışmaların uygunluk kriterleri belirlenirken çalışmaların
özetleri okunmuş, özet bilgilerin yetersiz kaldığı durumlarda çalışmaların tamamı okunarak detaylı
bir biçimde analiz edilmiştir. Ek olarak, incelenen çalışmaların kullandığı referanslar taranmış ve
ilgili olabilecek diğer makaleler değerlendirilmiştir. Gerçekleştirilen bu işlemlerin ardından,
belirlenen 32 adet çalışma detaylı bir biçimde analiz edilmiştir.

3.1. Derleme Çalışmasının Amacı
Bu derleme çalışması, aşağıdaki araştırma sorularının yanıtlarını aramaktadır:
Q1: Doğal dilden programlama dili kodu üreten çalışmalarda hangi yaklaşımlar kullanılmaktadır?
Q2: Hangi doğal dil işleme teknikleri bu çalışmalarda kullanılmaktadır?
Q3: Kullanılan veri setleri ve bu veri setlerinin büyüklükleri nelerdir?
Q4: Yaklaşımlarda kullanılan yöntemlerin temel karakteristikleri nelerdir?
Q5: Çalışmaların performansları nasıl değerlendirilmiştir?

Belirlenen bu araştırma sorularına dayalı olarak, kapsamlı taramalar gerçekleştirilmiştir.