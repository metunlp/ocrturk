Bütün bu aşamalardan sonra, üç karakterden kısa sözcükler de
metinlerden atılmış ve sonrasında tüm sözcükler küçük harfli olacak
hale dönüştürülerek derlem eğitim için son halini almıştır. Orijinal
haber gövdesi ve başlığı ile ön işlenmiş haber gövdesi ve başlığı için
birer örnek sırasıyla Tablo 4 ve Tablo 5’te verilmiştir.
2.3. Transformatör Mimarisi (Architecture of Transformer)
Transformatör mimarisinin DDİ çalışmalarında kullanılan diğer
mimarilerden en büyük farklarından biri verileri işlediği zaman
adımındaki farklılıktır. Önceki RNN, LSTM ve GRU mimarilerinde
sözcük dizileri, yani haber gövdesi, t-1 zaman adımından gelen gizli
durum ile t zamanındaki girdi vektörünün işleme sokulması mantığı
üzerine tasarlanmaktadır [25]. Transformatör mimarisinde ise bütün
dizi aynı zaman adımında bir matris olarak modele girdi olarak alınır.
Doğal dil üzerindeki çalışmalarda önceki mimariler ile kullanılan
kodlayıcı-kod çözücü yapısı ise ortak olarak Transformatör
mimarisinde de kullanılmaktadır. Yine RNN, LSTM ve GRU
mimarilerindeki tekrarlayan sinir hücre yapılarının yerini, iki alt
katmandan oluşan N adet Transformatör kodlayıcı ve kod çözücü
blokları almaktadır. Transformatör mimarisi günümüzde, doğal dil ile
alakalı problemlerin çözümünde RNN, LSTM ve GRU gibi
mimarilere göre daha çok tercih edilir duruma gelmiştir. Bunun
nedeni, çalışmalarda Transformatör mimarisi kullanılarak diğer
mimarilere göre daha başarılı sonuçlar elde edilmesi ve mimari olarak
hala geliştirilmeye devam edilmesidir. Transformatör mimarisinin
bahsedilen önceki mimarilerden yapı olarak birçok farklılığı daha
bulunmaktadır. Günümüzde mimari olarak farklı geliştirilmeler
yapılmış, farklı Transformatör mimarileri de mevcuttur. Fakat bu
çalışmada orijinal makalede de kullanılan ve gerekli yetenekleri
sunabilen Şekil 5’teki temel Transformatör mimarisi tercih edilmiştir.
Transformatörlerde farklılık gösteren yapılardan operasyonel olarak
ilk sırada yer alan konumsal kodlama metodudur [26]. Deterministik
bilgisayar sistemleri doğal dili insanlar gibi metinsel veya fonetik
olarak algılayamamaktadır. Bu sebeple mevcut verimizi bilgisayarın 
anlayabileceği sayısal değerler şeklinde ifade etmemiz gerekmektedir.
Bu ihtiyaçtan kaynaklı modelin eğitimi aşamasında, derlemin
içeriğinden oluşturulan sözlüğün sözcük gösterimi oluşturulmalıdır.
Sözlüğü oluşturan sözcüklerin her biri, gösterimden belirlenen
boyutta, sayıda, kendisinin en yakınına konumlanan diğer sözcüklerle
skaler değerler şeklinde ifade edilen temsil vektörleri
oluşturulmaktadır. Bu temsil vektörleri, bilgisayar sistemlerinin doğal
dili anlayacak şekilde sayısallaştırılmasında en önemli adımlardan
biridir. Buraya kadar olan kısım diğer mimarilerde de ortak olarak
bulunmaktadır. Transformatör mimarisi ise konumsal metot ile her
sözcüğün cümledeki konum bilgisini ve sözcük temsillerinin
konumlarını kullanılarak, Eş. 1 ve Eş. 2’deki formül sayesinde
konumsal değer matrisini oluşturur. Daha sonra mevcut girdi dizi
matrisi ile konumsal değer matrisi toplanır. Bu sayede bağlama bağlı
olarak gramer yapısının çözümlenmesi sağlanmış olur. Aynı zamanda
eş sesli sözcüklerin cümledeki konumuna göre hangi anlamı ifade
ettiği bilgisayar tarafından anlaşılabilir olmaktadır. Ayrıca Şekil 6’da,
örnek olarak 32 sözcükten oluşan ve sözcük temsil boyutu 64 olan bir
girdi dizi matrisi için cümlenin konumsal değer matrisi gösterilmiştir. 

$$PE_{(pos, 2i)} = \sin(\text{pos} / 10000^{2i/d_{\text{model}}}) \quad (1)$$

$$PE_{(pos, 2i+1)} = \cos(\text{pos} / 10000^{2i/d_{\text{model}}}) \quad (2)$$

Transformatör mimarisinin, önceki mimarilerden farklılaşmasının
operasyonel olarak bir sonraki faktörü ise çok başlı öz dikkat
mekanizmasıdır. Bu mekanizma kısmen LSTM ve GRU gibi
mimarilerde ek katman olarak modele eklenen dikkat mekanizmasının
bir türevidir. Fakat Transformatör mimarisi, kodlayıcı ve kod çözücü
bloklarının alt katmanlarında çok başlı öz dikkat mekanizması
kavramı ile daha kapsamlı hesaplama yeteneğine sahip olmaktadır. Bu
adımda cümle içindeki her sözcüğün diğer sözcüklerle olan dikkat
matrisi Şekil 7’deki gibi Eş. 3’teki hesaplamalar yapılarak ağırlıklar
güncellenir. Bu hesaplamalarda sorgu (Q), anahtar (K) ve değer (V)
matrisleri parametre olarak kullanılır. İlk başta bu üç parametre Q, K
ve V aynı dizi matrisleriyken eğitim aşamasında farklılaşarak 

Tablo 4. Ön işlenmiş haber ve başlık örneği-1 (Pre-processed news and headline sample-1) 

<table>
  <thead>
    <tr>
      <th>&nbsp;</th>
      <th>Orijinal metin</th>
      <th>Ön işlenmiş metin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Haber</th>
      <td>
        Özel yetkili Ankara 12. Ağır Ceza Mahkemesi, 28 Şubat soruşturmasını yürüten savcıların itirazı üzerine, nöbetçi hakimlikçe serbest bırakılan emekli Orgeneral Teoman Koman ile emekli Korgeneraller Engin Alan ve Kamuran Orhon hakkında "yakalama kararı" çıkarttı. Mahkeme kararın gerekçesini "zanlılara atılı suçun niteliği" olarak belirtti. MHP'den milletvekili seçilen Alan, Balyoz davasından tutuklu bulunuyor.
      </td>
      <td>
        özel yetkili Ankara ağır ceza mahkemesi şubat soruşturmasını yürüten savcıların itirazı üzerine nöbetçi hakimlikçe serbest bırakılan emekli Orgeneral Teoman koman emekli korgeneraller engin alan Kamuran Orhon hakkında yakalama kararı çıkarttı mahkeme kararın gerekçesini zanlılara atılı suçun niteliği belirtti MHP den milletvekili seçilen alan balyoz davasından tutuklu bulunuyor
      </td>
    </tr>
    <tr>
      <th>Başlık</th>
      <td>
        28 Şubat komutanlarına yakalama kararı çıktı
      </td>
      <td>
        ### şubat komutanlarına yakalama kararı çıktı
      </td>
    </tr>
  </tbody>
</table>

Tablo 5. Ön işlenmiş haber ve başlık örneği-2 (Pre-processed news and headline sample-2) 

<table>
  <thead>
    <tr>
      <th>&nbsp;</th>
      <th>Orijinal metin</th>
      <th>Ön işlenmiş metin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Haber</th>
      <td>
        Türk Hava Yolları'nın 2016'nın ilk iki ayındaki yolcu sayısı geçen yılın aynı dönemine göre yüzde 11.2 artışla Türk hava yolları ilk ayındaki yolcu sayısı geçen sene 9.2 milyona ulaştı. Bu rakam 2015'te 8.3 milyon yılın aynı dönemine yüzde artışla milyona ulaşmış oldu. Yolcu sayısındaki artış iç hatlarda yüzde 12.6, rakam milyon olmuştu yolcu sayısındaki artış dış hatlarda yüzde 10.2 oranında gerçekleşti. Dış Hatlar hatlarda yüzde dış hatlarda yüzde oranında Business/Comfort Class yolcu sayısı ve Dıştan Dışa gerçekleşti dış hatlar business/comfort class yolcu Transfer Yolcu sayılarında da Ocak-Şubat 2015 sayısı dıştan dışa transfer yolcu sayılarında ocak dönemine kıyasla sırasıyla yüzde 5.8 ve 20.9 artış şubat dönemine kıyasla sırasıyla yüzde artış sağlandı. Doluluk oranı 3 puanlık düşüş ile yüzde 73.3 sağlandı doluluk oranı puanlıklık düşüş yüzde oldu oldu.
      </td>
      <td>
        Türk hava yolları ilk ayındaki yolcu sayısı geçen sene 9.2 milyona ulaştı. Bu rakam 2015'te 8.3 milyon yılın aynı dönemine yüzde artışla milyona ulaşmış oldu. Yolcu sayısındaki artış iç hatlarda yüzde 12.6, rakam milyon olmuştu yolcu sayısındaki artış dış hatlarda yüzde 10.2 oranında gerçekleşti. Dış Hatlar hatlarda yüzde dış hatlarda yüzde oranında business/comfort class yolcu sayısı ve dıştan dışa gerçekleşti dış hatlar business/comfort class yolcu transfer yolcu sayılarında ocak-şubat 2015 sayısı dıştan dışa transfer yolcu sayılarında ocak dönemine kıyasla sırasıyla yüzde 5.8 ve 20.9 artış şubat dönemine kıyasla sırasıyla yüzde artış sağlandı. Doluluk oranı 3 puanlık düşüş ile yüzde 73.3 sağlandı doluluk oranı puanlıklık düşüş yüzde oldu oldu.
      </td>
    </tr>
    <tr>
      <th>Başlık</th>
      <td>
        THY yolcu sayısını 9.2 milyona çıkardı
      </td>
      <td>
        THY yolcu sayısını ### milyon a çıkardı
      </td>
    </tr>
  </tbody>
</table>