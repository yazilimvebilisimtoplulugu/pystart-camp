# --- Soru 5: kutuphane.py ---

%%writefile kutuphane.py

class KitapBulunamadi(Exception):
    pass


class KitapMusaitDegil(Exception):
    pass


class Kitap:
    def __init__(self, baslik, yazar, yil):
        self.baslik = baslik
        self.yazar = yazar
        self.yil = yil
        self.odunc_mu = False

    def odunc_ver(self):
        if self.odunc_mu:
            raise KitapMusaitDegil(
                f"'{self.baslik}' zaten ödünç verilmiş."
            )

        self.odunc_mu = True

    def iade_et(self):
        self.odunc_mu = False

    def __str__(self):
        durum = "Ödünçte" if self.odunc_mu else "Rafta"

        return f"{self.baslik} - {self.yazar} ({self.yil}) [{durum}]"


class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def __iter__(self):
        return iter(self.kitaplar)

    def kitap_bul(self, baslik):
        for kitap in self.kitaplar:
            if kitap.baslik.lower() == baslik.lower():
                return kitap

        raise KitapBulunamadi(
            f"'{baslik}' isimli kitap bulunamadı."
        )

    def ara(self, kelime):
        bulunanlar = []

        for kitap in self.kitaplar:
            if kelime.lower() in kitap.baslik.lower():
                bulunanlar.append(kitap)

        return bulunanlar

    def odunc_ver(self, baslik):
        kitap = self.kitap_bul(baslik)
        kitap.odunc_ver()

    def iade_al(self, baslik):
        kitap = self.kitap_bul(baslik)
        kitap.iade_et()

    def musait_kitaplar(self):
        for kitap in self.kitaplar:
            if not kitap.odunc_mu:
                yield kitap

    def kaydet(self):
        with open("kitaplar.txt", "w", encoding="utf-8") as dosya:
            for kitap in self.kitaplar:
                durum = 1 if kitap.odunc_mu else 0

                dosya.write(
                    f"{kitap.baslik};{kitap.yazar};{kitap.yil};{durum}\n"
                )

    def yukle(self):
        try:
            with open("kitaplar.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    baslik, yazar, yil, durum = satir.strip().split(";")

                    kitap = Kitap(baslik, yazar, int(yil))
                    kitap.odunc_mu = bool(int(durum))

                    self.kitaplar.append(kitap)

        except FileNotFoundError:
            pass
