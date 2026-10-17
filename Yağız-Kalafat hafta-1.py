
name=str(input("isiminizi giriniz: "))
surname=str(input("soyadınızı giriniz: "))
major=str(input("bölümünüzü giriniz: "))
day=int(input("doğum gününüzü giriniz: "))
month=int(input("doğum ayınızı giriniz: "))
year=int(input("doğum yılınızı giriniz: "))

doğum_tarihi=(day,month,year)
age=(2026-doğum_tarihi[2])

name=name.title()
surname=surname.title()
major=major.title()

print(f"{name} {surname}")
print(major)
print(f"{doğum_tarihi[0]:02d}.{doğum_tarihi[1]:02d}.{doğum_tarihi[2]:04d}")
print(age)

##############################################################################

sentence=str(input("cümle giriniz: "))

length=len(sentence)
wlength=len(sentence.replace(" ", ""))
words=sentence.split()
sentence=sentence.upper()
sentence=sentence[::-1]
a=sentence.lower().count("a")
b="python" in sentence.lower() 

print(length)
print(wlength)
print(len(words))
print(f"ilk kelime:{words[0]}" f"\nson kelime:{words[-1]}")
print(sentence)
print(f"a sayısı:{a}")
print(f"python kelimesi varmı:{b}")

#içinde büyük i olan cümlelerde i harfi I bu şekilde gözüküyor.

###############################################################

notlar=(input("3 tane notu aralarında boşluk bırakarak yaz: "))
not_listesi=[float(notlar) for notlar in notlar.split()]
yeni_not=float(input("bir not daha ekle: "))
not_listesi.append(yeni_not)
not_listesi.sort()
a=max(not_listesi)
b=min(not_listesi)
ort=(sum(not_listesi)/len(not_listesi))

print(f"sıralı liste: {not_listesi}")
print(f"en yüksek not: {a}")
print(f"en düşük not: {b}")
print(f"ortalama: {ort}")

not_listesi.pop(0)
yeni_ort=(sum(not_listesi)/len(not_listesi))
print(f"en düşük not çırarıldı: {not_listesi}")
print(f"yeni ortalama: {yeni_ort}")

##################################################################

rehber = {'Ali': '0555 111 22 33', 'Ayşe': '0532 444 55 66'}
yeni_isim=input("isim: ")
yeni_telefon=input("telefon: ")
rehber[yeni_isim]=yeni_telefon
print(rehber)

rehber['Ali']='0555 999 88 77'
print(rehber)

silinen_numara=rehber.pop("Ayşe")
print(f"silinen numara: {silinen_numara}")

a=input("isim giriniz: ")
if(a in rehber):
    print(f"aradığınız numara: {rehber[a]}")
else:
    print("kayıt bulunamadı")

print(f"kişi sayısı: {len(rehber)}")
print(sorted(rehber))

#########################################################

hobi1=input("hobilerinizi virgül kullanarak giriniz: ")
hobi2=input("hobilerinizi virgül kullanarak giriniz: ")

kişi1=set(hobi1.strip() for hobi1 in hobi1.split(","))
kişi2=set(hobi2.strip() for hobi2 in hobi2.split(","))

ort=sorted(kişi1 & kişi2)
yalnız1=sorted(kişi1-kişi2)
yalnız2=sorted(kişi2-kişi1)
tümü=sorted(kişi1|kişi2)

print(f"ortak hobiler: {ort}")
print(f"sadece 1. kişideki hobiler: {yalnız1}")
print(f"sadece 2. kişideki hobiler: {yalnız2}")
print(f"tüm hobiler: {tümü}")

ortak=len(kişi1 & kişi2)>0
eşit=len(kişi1)==len(kişi2)
a=len(kişi1) and len(kişi2)>=3
b="satranç" in (kişi1 or kişi2)

print(ortak)
print(eşit)
print(a)
print(b)

#yaparken yapay zeka desteği aldım