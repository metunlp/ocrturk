<table>
<tr>
<td><b>Kaynak</b></td>
<td><b>Büyüklük</b></td>
<td><b>Türkçe içerik</b></td>
<td><b>Açıklama</b></td>
</tr>

<tr>
<td>Common Crawl¹</td>
<td>yaklaşık 3.15 milyar web sayfası (380 TiB) [8]</td>
<td>%0.7897 [9]</td>
<td>Kâr amacı gütmeyen kuruluş.</td>
</tr>

<tr>
<td>BookCorpus [10]</td>
<td>11,000 kitap, 985 milyon kelime.</td>
<td>bilinmiyor</td>
<td>OpenAI'nin ilk GPT modeli için kullanıldı.</td>
</tr>

<tr>
<td>C4 ve T5 [11]</td>
<td>745 GB.</td>
<td>Sadece İngilizce veri.</td>
<td>Common Crawl verisinin temizlenmiş hâli. Google tarafından yayımlanmıştır.</td>
</tr>

<tr>
<td>Openwebtext</td>
<td>8 milyon doküman, 38GB veri.</td>
<td>Sadece İngilizce veri.</td>
<td>GPT-2'nin eğitildiği Webtext’e alternatif olarak hazırlanmıştır.</td>
</tr>

<tr>
<td>RedPajama [12]</td>
<td>1.2 Trilyon belirtke.</td>
<td>bilinmiyor</td>
<td>Diğer büyük kaynaklardan veriseti oluşturmayı sağlayan proje.</td>
</tr>

<tr>
<td>Vikipedi</td>
<td>731 MB.</td>
<td>Sadece Türkçe veri.</td>
<td>Bu çalışmada kullanılmıştır.</td>
</tr>
</table>

Tablo 1: Açık erişimli metin kaynakları.

tilmi¸s T5, BERT, BART, GPT-2 ve BLOOM gibi
önemli modeller yer almaktadır

Türkçe metinlerden veriseti oluşturma

Hâlihazırda açık erişimle sunulan veriseti içinde Türkçe içeriğin hiç olmaması ya da çok az yer alması nedeniyle büyük dil ağları araştırmalarında kullanmak üzere sıfırdan bir veriseti oluşturmak elzem olmaktadır.  
Bu çalışmada yer alan deneyler yürütülmek için böyle bir veriseti sadece Vikipedi (Wikiptedia Türkçe sürümü) makaleleri kullanılarak gerçekleştirilmiştir.

Bunun için, güncel ve sıkıştırılmış `trwiki2` arşivi indirilmiş ardından bir Python betiği yardımıyla json formatında veriseti oluşturulmuştur.  
731 MB büyüklüğündeki bu veride ön işleme ve temizlik yapıldıktan sonra farklı uzunluklarda toplam 818.454 adet metin elde edilmiştir.

Bu metinler, tiktoken modülü [16] ile belirteçleştirilince 296.1 milyon belirteç oluşmuştur.  
Bu sonuç, GPT-2 modellerinde kullanılan  r50k_base kodlamasıyla elde edilmiştir.  
GPT-3.5 ve GPT-4'te kullanılan cl100k_base ile belirteç sayısı 242.6 milyon olmaktadır.  
Bu da Türkçe için daha uygun olduğu düşünülebilir.

---

Belirteçleştirme (Tokenization)

Sözcüksel analizde bir girdi metni oluşturan parçaların sınıflandırılması ve ayırt edilmesi işlemidir.  
Oluşturulan belirteçler bir sonraki işlemde kullanılırlar.

Girdi verisinden yer alan tüm veri belirteçlere ayrılarak bir sözvarlığı seti oluşturulur.  
Büyük dil modellerinin eğitilmesinde kullanılan verisetlerinde çoğunlukla Byte-Pair Encoding (BPE) belirteçleştirme algoritması uygulanmaktadır.

---

3. Modellerinin eğitilmeleri ve ince ayarlanmaları

Açık erişimli büyük dil modelleri

Ticari büyük dil modelleri dışında bazı gruplar tarafından açıkça paylaşılan büyük modeller de mevcuttur.  
Bunlar arasında Meta tarafından yayımlanan LLaMa [17] ailesinin 7, 13, 33 ve 65 milyar parametreli sürümleri bulunmaktadır.

Bu modeller 1 ve 1.4 trilyon belirteç ile eğitilmiştir.  
Ne yazık ki eğitim verisinde yer alan 20
