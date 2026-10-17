ad = input("Adınız: ")
soyad = input("Soyadınız: ")
bolum = input("Bölümünüz: ")
gun = input("Doğum günü: ")
ay = input("Doğum ayı: ")
yil = input("Doğum yılı: ")

yas = 2026 - int(yil)

print("========================================")
print("PyStart Katılımcı Kartı")
print("========================================")
print("Ad Soyad:", ad, soyad)
print("Bölüm:", bolum)
print("Doğum:", gun, ".", ay, ".", yil)
print("Yaş:", yas)
print("========================================")


cumle = input("Bir cümle yazın: ")

print("Karakter sayısı:", len(cumle))
print("Büyük harfli:", cumle.upper())
print("Küçük harfli:", cumle.lower())
print("A harfi sayısı:", cumle.count("a"))


not1 = int(input("1. not: "))
not2 = int(input("2. not: "))
not3 = int(input("3. not: "))

notlar = [not1, not2, not3]

yeni_not = int(input("Bir not daha ekle: "))
notlar.append(yeni_not)

notlar.sort()
print("Sıralı notlar:", notlar)

toplam = notlar[0] + notlar[1] + notlar[2] + notlar[3]
ortalama = toplam / 4
print("Ortalama:", ortalama)


rehber = {"Ali": "0555 111 22 33", "Ayşe": "0532 444 55 66"}

isim = input("Eklenecek isim: ")
numara = input("Numara: ")
rehber[isim] = numara

rehber["Ali"] = "0555 999 88 77"

del rehber["Ayşe"]

aranan = input("Aranacak isim: ")
if aranan in rehber:
  print("Numara:", rehber[aranan])
else:
  print("Kayıt bulunamadı")

print("Kişi sayısı:", len(rehber))


hobi1_str = input("1. kişinin hobileri: ")
hobi2_str = input("2. kişinin hobileri: ")

hobi1 = set(hobi1_str.split(","))
hobi2 = set(hobi2_str.split(","))

print("Ortak hobiler:", hobi1 & hobi2)
print("Tüm hobiler:", hobi1 | hobi2)