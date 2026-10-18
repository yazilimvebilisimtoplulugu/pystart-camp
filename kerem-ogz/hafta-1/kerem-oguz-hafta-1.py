Ad = input("Ad: ")
Soyad = input("Soyad: ")
bölüm = input("Bölüm: ")
gun = input("Doğum günü: ")
ay = input("Doğum ayı: ")
yil = input("Doğum yılı: ")
doğum = (gun, ay, yil)
yaş = 2026 - int(yil)
print("PyStart Katılımcı Kartı")
print("Ad Soyad    :", Ad, Soyad)
print("Bölüm       :", bölüm)
print("Doğum       :", doğum[0] + "." + doğum[1] + "." + doğum[2])
print("Yaş         :", yaş)
cümle = input("iyimisin: ")
print(len(cümle), len(cümle.replace(" ", "")))
gretting = cümle.split()
print(len(gretting), gretting[0], gretting[-1])
print(cümle.upper(), cümle[::-1])
print(cümle.lower().count("a"))
print("python" in cümle.lower())
# Gözlemim
# gözlemimde i harfi buyuk yazılmıyor yani ingilizce kurallarına uyuyor
metin = input("3 notu aralarında boşluk bırakarak yaz: ")
parcalar = metin.split()
notlar = [int(parcalar[0]), int(parcalar[1]), int(parcalar[2])]

yeni = int(input("Bir not daha ekle: "))
notlar.append(yeni)

notlar.sort()
print("Notlar (sıralı):", notlar)

print("En düşük:", min(notlar), "| En yüksek:", max(notlar))
print("Ortalama:", round(sum(notlar) / len(notlar), 2))

notlar.remove(min(notlar))
print("En düşük not çıkarıldı:", notlar)
print("Yeni ortalama:", round(sum(notlar) / len(notlar), 2))
rehber = {'Ali': '0555 111 22 33', 'Ayşe': '0532 444 55 66'}

isim = input("Eklenecek isim: ")
numara = input("Numara: ")
rehber[isim] = numara

rehber['Ali'] = '0555 999 88 77'

silinen = rehber.pop('Ayşe')
print("Silinen numara:", silinen)

aranan = input("Aranacak isim: ")
print(rehber.get(aranan, "Kayıt bulunamadı"))

print("Kişi sayısı:", len(rehber))
print("İsimler:", sorted(rehber))
hobi1 = input("1. kişinin hobileri: ")
hobi2 = input("2. kişinin hobileri: ")

# yazıları kümeye çevir
kume1 = set(hobi1.split(","))
kume2 = set(hobi2.split(","))

ortak = kume1.intersection(kume2)
sadece1 = kume1.difference(kume2)
sadece2 = kume2.difference(kume1)
hepsi = kume1.union(kume2)

print("Ortak hobiler:", sorted(ortak))
print("Sadece 1. kişide:", sorted(sadece1))
print("Sadece 2. kişide:", sorted(sadece2))
print("Tüm hobiler:", sorted(hepsi))

print("Ortak hobiniz var mı?", len(ortak) > 0)
print("Hobi sayılarınız eşit mi?", len(kume1) == len(kume2))
print("İkiniz de en az 3 hobi yazdınız mı?", len(kume1) >= 3 and len(kume2) >= 3)
print("satranç ikinizden birinin hobisi mi?", "satranç" in hepsi)
