class Kitap:
    kitap_listesi = []
    musait_kitaplar_listesi = []
    raftakiler = []
    kitap_listesi_selfli0 = []
    # Kodunuzu buraya yazınız
    def __init__(self,baslik,yazar,yil,odunc_mu = False):
        self.baslik = baslik
        self.yazar = yazar
        self.yil = yil
        self.odunc_mu = "Rafta"
        self.odunc_mu_sayisal = "0"
        var_mi = False
        open("kitaplar.txt","a",encoding="utf-8")
        with open("kitaplar.txt","r",encoding="utf-8") as file:
             satirlar = file.readlines()
             for satir in satirlar:
                  if satir.split(";")[0] == self.baslik:
                       var_mi = True
             if var_mi == False:
                            with open("kitaplar.txt","a",encoding="utf-8") as file2:
                                 file2.write(f"{self.baslik};{self.yazar};{self.yil};{self.odunc_mu_sayisal}\n")
        try:
          if not isinstance(yil,int):
               raise ValueError("Sayısal değer girmelisiniz")
        except ValueError as ex:
              print(ex)
              return 
        self.kitap_listesi.append(self.baslik)
        self.musait_kitaplar_listesi.append(self)
        self.kitap_listesi_selfli0.append(self)
    def odunc_al(self):
            self.odunc_mu = "Ödünç"
            self.odunc_mu_sayisal = "1"
            self.musait_kitaplar_listesi.remove(self)
            self.guncelle()    
    def iade_et(self):
            self.odunc_mu = "Rafta"
            self.odunc_mu_sayisal = "0"
            self.musait_kitaplar_listesi.append(self)
            self.guncelle()
    def __str__(self):
        return f"{self.baslik} - {self.yazar} ({self.yil}) [{self.odunc_mu}]"
    def guncelle(self):
         with open("kitaplar.txt","r+",encoding="utf-8") as file:
              satirlar = file.readlines()
              for i in range(len(satirlar)):
                   if satirlar[i].split(";")[0] == self.baslik:
                        satirlar[i] = f"{self.baslik};{self.yazar};{self.yil};{self.odunc_mu_sayisal}\n"
         with open("kitaplar.txt","w",encoding="utf-8") as file2:
            file2.writelines(satirlar)

                   




def musait_kitaplar():
     for kitap in Kitap.musait_kitaplar_listesi:
          yield kitap.baslik

def raftakiler():
     for kitap in Kitap.musait_kitaplar_listesi:
          yield kitap.baslik
     
     
            
class Kutuphane():
    kitaplistesi = []
    kitaplistesi_sadece_Selfli = [] # burayı ekleme sebebim araştırdım ve self.kitap şeklinde ekleyince sadece isim gidiyordu ödünç verme iade alma durumunda işime yaramazdı bende böyleli yaptım bi tane
    def __init__(self,kitap,odunc_mu=False):
        self.kitap = kitap
        self.odunc_mu = odunc_mu
        self.kitaplistesi.append(self.kitap)
        self.kitaplistesi_sadece_Selfli.append(self)
    def odunc_durumu(self,baslik):
        self.baslik = baslik
        if self.odunc_mu == True:
                raise KitapMusaitDegil("Bu kitap zaten ödünçte müsait değil.")
        else:
                self.odunc_mu = True
                print(f"{self.kitap} adlı kitap başarıyla ödünç verildi.")
    def iade_durumu(self,baslik):
        self.baslik = baslik
        if self.odunc_mu == True:
            print(f"{self.kitap} adlı kitabın iadesi alınıp rafa eklendi")
            self.odunc_mu = False
        else:
            self.odunc_mu = False
            raise KitapMusaitDegil("Bu kitap zaten rafta")
    def kaydet():
        kayit_isim = input("Kaydetmek istediğiniz kitabın ismini giriniz : ")
        kitap_yazar = input("Kitabın yazarını giriniz : ")
        kitap_yil = int(input("Kitabın hangi yılda çıktığını yazınız : "))
        kayit_isim = Kitap(kayit_isim,kitap_yazar,kitap_yil,odunc_mu=False)
        print(f"{kayit_isim} adlı kitap başarıyla eklendi.")
    def yukle():
        try:
            with open("kitaplar.txt","r",encoding="utf-8") as file:
                for i in file:
                 print(i)
        except FileNotFoundError:
            print("Rafta kitap yok")
    def __iter__(self):
         return self
         
def listele():
    for x in Kutuphane.kitaplistesi:
         print(x)




def kitap_ekle(kitap):
    kitap = Kutuphane(kitap)
    print(f"{kitap.kitap} adlı kitap başarıyla eklendi")

def kitap_bul(baslik=str):
    baslik.lower()
    for x in range(len(Kutuphane.kitaplistesi)):
        if baslik == Kutuphane.kitaplistesi[x]:
            print(f"{baslik} adlı aradığınız kitap bulundu")
            break
    else:
        raise KitapBulunamadi("Aradığınız kitap kütüphanede mevcut değil")



def ara(kelime=str):
    kelime = kelime.lower()
    i = 0
    for kitap in Kitap.kitap_listesi_selfli0:
         if kelime in kitap.baslik.lower():
              i+=1
              print(f"{i}. {kitap}")
    if i == 0:
         print("Aradığınız kelimeyi içeren kitap bulunamadı")


def odunc_ver(baslik):
    for k in Kutuphane.kitaplistesi_sadece_Selfli:
        if k.kitap == baslik:
            k.odunc_durumu(baslik)
            break
    else:
        raise KitapBulunamadi("Bu kitap kütüphanede bulunmuyor") or KitapMusaitDegil("Bu kitap zaten ödünçte müsait değil.")
                
def iade_al(baslik):
    for k in Kutuphane.kitaplistesi_sadece_Selfli:
       if k.kitap == baslik:
           k.iade_durumu(baslik)
           break
       else:
           raise KitapMusaitDegil("Bu kitap zaten rafta")



class KitapBulunamadi(Exception):
    pass

class KitapMusaitDegil(Exception):
    pass
