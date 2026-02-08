# TABLO I: İnce ayar veri kümesinden örnekler

<table>
<tr>
<td>
<b>GQA</b><br>
<b>Kullanıcı:</b> Gökyüzü karanlık mı?<br>
<b>Model:</b> Evet<br><br>

<b>Kullanıcı:</b> Sokakta ne var?<br>
<b>Model:</b> Araba<br><br>

<b>Kullanıcı:</b> Caddede otobüs var mı?<br>
<b>Model:</b> Hayır<br><br>

<b>Kullanıcı:</b> Trafik sinyali sağda mı yoksa solda mı?<br>
<b>Model:</b> Sol
<img src="figures/fig1.png" alt="" style="width:200px;">
</td>

<td>
<b>CosmosVQA</b><br>
<b>Kullanıcı:</b> Kitabın ismini öğrenebilir miyim?<br>
<b>Model:</b> Masumiyet Müzesi<br><br>

<b>Kullanıcı:</b> Bu kitap hangi türde bir kitaptır?<br>
<b>Model:</b> Aşk romanı<br><br>

<b>Kullanıcı:</b> Bu kitabın yazarı kimdir?<br>
<b>Model:</b> Orhan Pamuk
<img src="figures/fig2.png" alt="" style="width:200px;">
</td>

<td>
<b>VG</b><br>
<b>Kullanıcı:</b> Lütfen bu bölge için kısa bir açıklama yapınız: [0.69 0.35, 0.79, 0.69].<br>
<b>Model:</b> Bu bir insan.<br><br>

<b>Kullanıcı:</b> Lütfen bu cümlenin tanımladığı bölgenin sınırlarını koordinat veriniz: tenis kortundaki beyaz çizgi.<br>
<b>Model:</b> [0.0, 0.7, 0.9, 0.82]
<img src="figures/fig3.png" alt="" style="width:200px;">
</td>

<td>
<b>COCO</b><br>
<b>Kullanıcı:</b> Lütfen bu bölge için kısa bir açıklama yapınız: [0.3, 0.36, 0.62, 0.59].<br>
<b>Model:</b> Fotoğrafa bakan bir bilgisayar ekranı.<br><br>

<b>Kullanıcı:</b> Lütfen bu cümlenin tanımladığı bölgenin sınırlarını koordinat veriniz: en sağdaki ekran.<br>
<b>Model:</b> [0.3, 0.36, 0.62, 0.59]
<img src="figures/fig4.png" alt="" style="width:200px;">
</td>

<td>
<b>CC3M</b><br>
<b>Kullanıcı:</b> Sunulan görüntüyü temel alarak kompozit bir anlatı oluşturun.<br>
<b>Model:</b> çiftler için toplu nikah töreni düzenlendi.
<img src="figures/fig5.png" alt="" style="width:200px;">
</td>
</tr>
</table>

Şekil 1: Eğitimlere Ait Loss Grafikleri

![](figures/fig6.png)


A. Hakem: Dil Modeli

Bu çalışmanın yapıldığı Ağustos 2024 tarihinde çoğu ölçüme göre en iyi dil modeli olan OpenAI’ın GPT-4o [15] modeli hakem olarak kullanılmıştır. Sorular, resimler ve modellerin verdikleri cevaplar hakem olarak belirlenen GPT-4o modeline verilerek modelin yanıtı ne kadar doğru olduğuna göre 100 üzerinden bir puan vermesi istenmiştir. GPT-4o’ya puanlattırmak için kullanılan talimat formatı aşağıdaki gibidir:

{görsel}

Soru: {soru}

Cevap: {model-cevabı}

![](figures/fig7.png)

Şekil 2: İnce Ayar Eğitiminde Learning Rate’in Değişimi

Bir görsel, görselle ilgili bir soru ve verilen cevap gösterilmiştir. Çok iyi kaliteli cevaplara 100, iyilere 80, ortalamalara 30, kötülere 0 puan ver. Sadece puanı tam sayı olarak yaz, hiçbir açıklama yapma.

Ardından GPT-4o’nun verdiği yanıt ile modelin o soruya ne kadar iyi yanıt verdiği 100 üzerinden bir puan ile ölçülmüştür. GPT-4o modelinin yanıtları deterministik olmaması ve aynı cevaba farklı puanlar verilebilmesi nedeniyle her soru için 5 kez değerlendirme yapılarak bu değerlendirmelerde verilen puanların ortalaması alınmıştır.

Bu puanlama için kullanılan test kümesi 4 alt kümeden oluşmaktadır: OCR, Kompleks, Tanımlama ve Detay. Bu kümelerin içeriği aşağıda açıklanmıştır:

OCR: Toplam 10 kitap içeren bu veri kümesi, her kitap için gerçek hayatta çekilmiş bir adet fotoğraf ile bir dijital kapak görselini içermektedir. Veri kümesi, kitabın kapağında yer alan yazıların ne olduğunu sorgulayan 20 sorudan oluşmaktadır.

Kompleks:Bu kategori, modelin görsel içeriklere dayanarak üst düzeyde akıl yürütme ve çıkarımlar 



