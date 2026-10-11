# PyStart Python Kampı ..

Selam! Düzce Üniversitesi Yazılım ve Bilişim Topluluğu'nun 3 haftalık Python kampına hoş geldin. Videoları kendi hızında izleyecek, her hafta küçük bir ödev çözecek ve çözümünü buraya yükleyeceksin. Hazırsan başlayalım.

## Eğitim

Kampta BTK Akademi'deki **Sıfırdan İleri Seviye Python Programlama** eğitiminin ilk 14 modülünü bitireceğiz.

- [Eğitim sayfası](https://www.btkakademi.gov.tr/portal/course/sifirdan-ileri-seviye-python-programlama-5877)
- [Ders oynatıcı](https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877)

Eğitim tamamen ücretsiz, BTK Akademi hesabınla giriş yapman yeterli. 15. modül (İleri Seviye Python Modülleri) ve sonrası bu kampın konusu değil; onlara şimdilik takılma.

## Haftalık program

Kamp **11 Ekim 2026 Pazar** günü başlıyor ve 3 hafta sürüyor. Ödevlerini her hafta **Cumartesi 23.59**'a kadar göndermen yeterli.

| Hafta | Modüller | Video süresi | Ödev son teslim |
| --- | --- | --- | --- |
| 1 | 1. Tanıtım<br>2. Gerekli Ortamın Hazırlanması<br>3. Python Objeleri ve Veri Yapıları<br>4. Python Operatörleri | 4 sa 45 dk | 17 Ekim Cumartesi, 23.59 |
| 2 | 5. Koşul İfadeleri<br>6. Döngüler<br>7. Fonksiyonlar | 3 sa 39 dk | 24 Ekim Cumartesi, 23.59 |
| 3 | 8. Nesne Tabanlı Programlama<br>9. Modüller<br>10. Hata ve Hata Yönetimi<br>11. Dosya Yönetimi<br>12. Fonksiyonlarda ileri konular (iç içe fonksiyonlar, decorator)<br>13. Iterators<br>14. Generators | 4 sa 37 dk | 31 Ekim Cumartesi, 23.59 |

Küçük bir tavsiye: videoları haftaya yay. Günde 45 dakika kadar video izleyip en az o kadar da kod yazarsan hafta rahat geçer. 3. modül tek başına 3 saat sürüyor, ilk haftayı son güne bırakma.

## Çalışırken

- **Not al.** Her dersin sonunda öğrendiklerini kendi cümlelerinle birkaç satır yaz; ödevde en çok bu notlar işine yarayacak.
- **Kodu kendin yaz.** Eğitmen kod yazarken videoyu durdur, aynısını kendi bilgisayarında yazıp çalıştır. Kopyala-yapıştır yapma, bırak parmakların alışsın.

## Ödevleri nasıl göndereceksin?

1. Her hafta ödev notebook'u (`Hafta_1_Odevi.ipynb` gibi) duyuru kanalına gelecek. Son teslim o haftanın Cumartesi günü, saat 23.59.
2. Notebook'u indir, çözümlerini soruların altındaki kod hücrelerine yaz. Göndermeden önce bütün hücreleri bir kez çalıştır ki çıktılar notebook'ta görünsün.
3. Notebook'unu bu repoda kendi adının olduğu klasöre **Fork** ve **Pull Request** ile gönder. Bunlar ne demek, hemen aşağıda anlattık.
4. Ekip sonrasında PR'ına bakıp birleştirir (merge). Sonra klasörün burada görünür.

Notebook'u VS Code (Python ve Jupyter eklentileriyle), Jupyter Notebook ya da Google Colab'da açabilirsin. `input()` olan bir hücreyi çalıştırınca altında küçük bir giriş kutusu açılır, cevabını oraya yazarsın.

### Fork ve Pull Request de ne?

Bu repoya doğrudan dosya ekleyemezsin ama dert değil. Şöyle düşün: topluluğun reposu ortak bir defter. Sen önce bu defterin fotokopisini alıyorsun (fork), ödevini kendi fotokopine yazıyorsun, sonra da ekibe "bunu asıl deftere de ekler misiniz?" diyorsun (Pull Request).

**Fork**, bu reponun senin GitHub hesabındaki kopyası. `github.com/yazilimvebilisimtoplulugu/pystart-camp` adresindeki reponun bir eşi `github.com/kullanici-adin/pystart-camp` adresinde oluşur. Kopya tamamen senin: istediğin gibi dosya ekle, sil, değiştir; asıl repo bundan etkilenmez.

**Pull Request (kısaca PR)**, kendi kopyanda yaptığın değişikliklerin asıl repoya alınması için gönderdiğin istek. Ekip eklediğin dosyalara bakar, uygunsa asıl repoya ekler. Bu son adıma **merge** (birleştirme) deniyor.

```
Topluluğun reposu
      │  Fork: repoyu kendi hesabına kopyalarsın
      ▼
Senin kopyan (fork)
      │  Ödev dosyalarını yüklersin
      │  Pull Request açarsın
      ▼
Ekip inceler ve birleştirir (merge)
      │
      ▼
Klasörün topluluğun reposunda görünür
```

Neden bu kadar uğraş? Herkes kendi kopyasında çalışınca kimse yanlışlıkla başkasının ödevini silemiyor. Üstelik açık kaynak projelere de tam olarak böyle katkı veriliyor; yani burada öğrendiğin şey ileride gerçek projelerde de işine yarayacak.

Bir terim daha: **Commit**, yaptığın değişikliği kaydetmek demek. Dosyayı yükledikten sonra **Commit changes**'e basmayı unutma, yoksa dosyaların kaydedilmez.

### Klasör yapısı

Herkesin kendi adıyla bir klasörü var, içinde de her hafta için ayrı bir klasör:

```
ayse-yilmaz/
├── hafta-1/
│   └── Hafta_1_Odevi.ipynb
├── hafta-2/
│   └── Hafta_2_Odevi.ipynb
└── hafta-3/
    ├── Hafta_3_Odevi.ipynb
    ├── kutuphane.py
    └── kitaplar.txt
```

3. haftada notebook'un oluşturduğu `kutuphane.py` ve `kitaplar.txt` dosyalarını da eklemeyi unutma.

Klasör adını `ad-soyad` şeklinde yaz: küçük harf, boşluk yerine tire, Türkçe karakter yok. Yani `Ayşe Yılmaz` → `ayse-yilmaz`.

Nasıl göründüğünü merak ediyorsan repodaki [`enes-sarpun`](enes-sarpun) klasörüne göz at. İçindeki `.gitkeep` dosyaları sadece boş klasörler görünsün diye orada, senin eklemene gerek yok.

### İlk hafta: adım adım

Hepsi tarayıcıdan yapılıyor, Git kurmana gerek yok.

1. [github.com](https://github.com)'dan ücretsiz bir hesap aç (zaten varsa bu adımı geç).
2. Bu sayfanın sağ üstündeki **Fork** düğmesine, sonra **Create fork**'a tıkla. Repo artık senin hesabında da var.
3. Bilgisayarında `ad-soyad` adında bir klasör aç, içine `hafta-1` klasörünü oluştur ve doldurduğun `Hafta_1_Odevi.ipynb` dosyasını oraya koy.
4. Kendi fork'unda **Add file → Upload files**'a tıkla, `ad-soyad` klasörünü sayfaya sürükleyip bırak ve **Commit changes**'e bas.
5. Fork'unun ana sayfasında **Contribute → Open pull request**'e tıkla. Başlığa `Hafta 1 - Ad Soyad` yaz ve **Create pull request**'e bas. Hepsi bu!

Klasör sürüklenmiyorsa şöyle yap: **Add file → Create new file**'a tıkla, dosya adı kutusuna `ad-soyad/hafta-1/README.md` yaz (her `/` yeni bir klasör açar), içine adını yazıp kaydet. Sonra oluşan `hafta-1` klasörüne gir ve **Add file → Upload files** ile notebook'unu yükle.

### Sonraki haftalar

1. Fork'unun ana sayfasında **Sync fork → Update branch**'e tıkla, kopyan güncellensin.
2. Kendi `ad-soyad` klasörüne gir ve **Add file → Upload files** ile yeni haftanın klasörünü (`hafta-2`, `hafta-3`) yükle.
3. `Hafta 2 - Ad Soyad` başlığıyla yeni bir Pull Request aç.

### Unutma

- Sadece kendi klasörüne dosya ekle; başkalarının klasörlerine ve bu README'ye dokunma.
- Repo herkese açık, o yüzden öğrenci numarası, telefon gibi kişisel bilgilerini dosyalara yazma.
- Gönderdikten sonra bir şey düzeltmek istersen yeni PR açmana gerek yok. Dosyayı fork'unda güncelle, açık olan PR kendiliğinden güncellenir.
- Diğer arkadaşlarının çözümleri de burada duruyor. Bakıp fikir almak serbest ama kendi çözümünü kendin yaz; asıl öğrenme orada.

Takıldığın bir yer olursa çekinmeden ekibe sor. Kolay gelsin!
