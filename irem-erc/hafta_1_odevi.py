#1.ödev
# Ad soyadı yaz.
adSoyad=input("Ad Soyad:")
ad=adSoyad.title()
# Bölümü yaz.
bolum=input("Bölüm:")
# Doğum tarihini yaz
gun = int(input("Doğum gününüz(örk:9): "))
ay = int(input("Doğum ayınız(örk:3): "))
a=yil = int(input("Doğum yılınız(örk:2007): ")) 
doğumTarihi=(gun,ay,yil)
r= "." .join([str(f"{gun:02d}"),str(f"{ay:02d}"),str(yil)])
# Yaşı hesapla.
Yaş=2026-a
# Katılımcı kartı
print("======================")
print("PyStart Katılımcı Kartı")
print("======================")
print(f"Ad Soyad:{ad}")
print(f"Bölüm:{bolum}")
print(f"Doğum : {r}")
print(f"Yaş:{Yaş}")
print("======================")

#2.ödev
message=input("Lütfen bir cümle giriniz:")
# Karakter sayısını bul.
print(f"Karakter sayısı:{len(message)}")
# Boşluksuz karakter sayısını bul.
a=message.replace(" ","")
print(f"Boşluksuz karakter sayısı:{len(a)}")
# Kelime sayısını bul.
b=message.split()
print(f"Kelime sayısı:{len(b)}")
# İlk kelimeyi bul.
print(f"İlk kelime:{b[0]}")
# Son kelimeyi bul.
print(f"Son kelime:{b[-1]}")
# Cümleyi tamamen büyük harfli ve tersten yaz
c=message.upper()
e=c[::-1]
print(f"Tersten büyük harfle yazılışı:{e}")
# Cümlede toplam ne kadar 'a' ve 'A' var?
d=message.lower()
result=d.count('a')
print(f"Toplam 'a' sayısı:{result}")
# 'python' kelimesi cümlenin içinde var mı? (True veya False döner)
s = 'python' in message
print(f"Cümlede 'python' kelimesi var mı?:{s}")

# Gözlem (python ingilizce dil desteği kullandığı için, 'i' harfini upper ile büyüttüğümüzde 'I'' olarak yazılır.

#3.ödev
# Üç not ekle.
metın=input("3 notu aralarında boşluk bırakarak yaz:")
b=metın.split()
not1=int(b[0])
not2=int(b[1])
not3=int(b[2])
# Bir not daha ekle.
not4=int(input("Bir not daha ekle:"))
# Notları sırala.
numbers=[not1, not2,not3,not4]
a=sorted(numbers)
print(f"Notlar (sıralı):{a}")
# En düşük notu yaz.
d=min(numbers)
print(f"En düşük:{d}")
# En yüksek notu yaz.
f=max(numbers)
print(f"En yüksek:{f}")
# Ortamayı al.
o=sum(numbers)/len(numbers)
print(f"ortalama:{o}")

# En düşük notu çıkar ve tekrar ortalamasını al.
v=min(numbers)
numbers.remove(v)
t=sum(numbers)/len(numbers)
print(f"En düşük not çıkarıldı:{numbers}")
print(f"Yeni ortalama:{t}")

#4.ödev
# Telefon rehberi 
rehber = {'Ali': '0555 111 22 33', 'Ayşe': '0532 444 55 66'}
# Bilgileri sor.
isim=input("İsimi giriniz:")
numara=input("Numarayı giriniz:")
rehber[isim]=numara
# Alinin numarasını değiştir.
rehber['Ali']='0555 999 88 77'
# Ayşenin nunarasını sil ve yazdır.
silinenNumara=rehber.pop('Ayşe')
print(f"Silinen Ayşenin numarası:{silinenNumara}")
# Kullanıcıdan yeni isim al.
arananIsim=input("Numarasını aradığınız isim giriniz:")
# Sonucu yaz.
sonuc=rehber.get(arananIsim,'Kayıt bulunamadı')
print(f"Aranan sonuç:{sonuc}")
# Rehberdeki kişi sayısını yaz.
print(f"rehberdeki kişi sayısı:{len(rehber)}")
# Alfabetik sırala.
print(f"rehberdeki kişilerin alfabetik sırası:{sorted(rehber.keys())}")

#5.ödev
# Kullanıcılardan hobileri virgülle ayrılmış olarak alma
kisi1 = input("1. Kişinin hobilerini girin (örn: futbol,satranç,müzik): ")
kisi2 = input("2. Kişinin hobilerini girin (örn: sinema,satranç,kitap): ")

# Setlere ayırma
kume1 = set(hobi.strip().lower() for hobi in kisi1.split(','))
kume2 = set(hobi.strip().lower() for hobi in kisi2.split(','))

# Ortak hobileri yaz.
ortakHobiler = kume1.intersection(kume2)
print("Ortak hobiler:", sorted(ortakHobiler))
# Yalnızca birinci kişide olanları yaz.
yalnizBirinci = kume1.difference(kume2)
print("Yalnızca birinci kişide olanlar:", sorted(yalnizBirinci))
# Yalnızca ikinci kişide olanları yaz.
yalnizIkinci = kume2.difference(kume1)
print("Yalnızca ikinci kişide olanlar:", sorted(yalnizİkinci))
# Tüm hobileri yaz.
tumHobiler = kume1.union(kume2)
print("Tüm hobiler:", sorted(tumHobiler))
print("-" * 40)

# True/False Soruları 
# Ortak hobiniz var mı?
soru1 = len(ortakHobiler) > 0
print("Ortak hobiniz var mı?:", soru1)
# Hobi sayılarınız eşit mi?
soru2 = len(kume1) == len(kume2)
print("Hobi sayılarınız eşit mi?:", soru2)
# İkiniz de en az 3 hobi yazdınız mı?
soru3 = len(kume1) >= 3 and len(kume2) >= 3
print("İkiniz de en az 3 hobi yazdınız mı?:", soru3)
# 'satranç' ikinizden birinin hobisi mi?
soru4 = 'satranç' in tumHobiler
print("'satranç' ikinizden birinin hobisi mi?:", soru4)




