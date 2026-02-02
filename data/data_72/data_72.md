2.6. Evrişimsel Sinir Ağları
Evrişimsel sinir ağları, çok boyutlu girdiler için ve özellikle iki boyutlu görsel veriler için
önerilmiş bir derin öğrenme yöntemidir (LeCun vd., 1998). Evrişimsel sinir ağları diğer sinir
ağlarına göre daha az sayıda nöron bağlantısına sahiptir ve birçok farklı sürümü literatürde
mevcuttur. Bu sinir ağları öğrenme aşamasında oldukça büyük boyutta işaretli veriye ihtiyaç
duymaktadır (Ravì vd., 2017). Bu derin öğrenme yöntemi doğal dil işleme alanındaki çeşitli
problemler üzerinde uygulanmış ve başarılı sonuçlar elde edilmiştir.
3. DOĞAL DİL İŞLEME ALANINDAKİ DERİN ÖĞRENME ÇALIŞMALARI

Derin öğrenmenin bir önceki bölümde anlatılan farklı yöntemlerinden özellikle yinelenen
sinir ağları ve evrişimsel sinir ağlarının doğal dil işleme problemlerini çözmede de başarılı sonuçlar
verdiği görülmüştür. Örneğin; evrişimsel sinir ağlarının doğal dil işlemenin çok farklı problemlerini
çözmede kullanılabileceği, çok görevli öğrenme için birleşik bir mimarinin tanıtıldığı bir çalışmada
gösterilmiştir (Collobert ve Weston, 2008). Bahsi geçen bu iki yöntemle birlikte; diğer derin
öğrenme yöntemlerinin de doğal dil işlemenin çeşitli problemlerinde kullanılabileceği ve bu
yöntemlere dayalı başarılı sistemlerin geliştirilebileceği, literatürdeki farklı çalışmalarda ifade
edilmiştir (Socher vd., 2012).
Bu bölümün aşağıdaki alt bölümlerinde de doğal dil işleme alanındaki örnek problemler ve bu
problemler için derin öğrenme yaklaşımlarının tanıtıldığı çalışmalara yer verilmiştir. Ayrıca, Tablo
2’de bu alt bölümlerde açıklanan problemler ve çözümünde kullanılan derin öğrenme yöntemleri
özet şeklinde sunulmuştur.

Tablo 2. Tanıtılan Doğal Dil İşleme Problemleri ve Kullanılan Derin Öğrenme Yöntemleri

<table>
  <tr>
    <td><strong>Doğal Dil İşleme Problemi</strong></td>
    <td><strong>Kullanılan Derin Öğrenme Yöntemleri</strong></td>
  </tr>

  <tr>
    <td>Metin Sınıflandırma</td>
    <td>
      • Evrişimsel Sinir Ağları<br>
      • Yinelemeli Evrişimsel Sinir Ağları<br>
      • LSTM ve Evrişimsel Sinir Ağları
    </td>
  </tr>

  <tr>
    <td>Metin Ayrıştırma</td>
    <td>• Evrişimsel Sinir Ağları</td>
  </tr>

  <tr>
    <td>Duygu Analizi</td>
    <td>
      • Derin Oto-Kodlayıcılar<br>
      • Evrişimsel Sinir Ağları
    </td>
  </tr>

  <tr>
    <td>Bilgi Çıkarımı</td>
    <td>• Derin Sinir Ağları</td>
  </tr>

  <tr>
    <td>Varlık İsmi Tanıma</td>
    <td>• LSTM ve Evrişimsel Sinir Ağları</td>
  </tr>

  <tr>
    <td>Zamansal İlişki Çıkarımı</td>
    <td>• Evrişimsel Sinir Ağları</td>
  </tr>

  <tr>
    <td>Olay Çıkarımı</td>
    <td>• Evrişimsel Sinir Ağları</td>
  </tr>

  <tr>
    <td>Sözcük Türü Etiketleme</td>
    <td>
      • Derin Sinir Ağları<br>
      • LSTM
    </td>
  </tr>

  <tr>
    <td>Metin Sıralama</td>
    <td>• Evrişimsel Sinir Ağları</td>
  </tr>

  <tr>
    <td><strong>Otomatik Harf Çevirisi</strong></td>
    <td>• Derin İnanç Ağları</td>
  </tr>

  <tr>
    <td>Otomatik Soru Cevaplama</td>
    <td>
      • Evrişimsel Sinir Ağları<br>
      • LSTM
    </td>
  </tr>
</table>
