class Ogrenci:
    def __init__(self): #objeyi oluşturduğumuz zaman çalışacak kodlar
        self.adi = ""
        self.soyadi = ""
        self.yasi = None
        self.sevdigi_renkler = []
        self.sozluk = {"yasi":self.yasi}
        print("Objeyi oluşturdum ! ")
        self.dogum_tarihi()

    def dogum_tarihi(self):
        print(2017-self.yasi)

ogrenci1 = Ogrenci()
print(ogrenci1.adi)
ogrenci1.adi = "batu"
print(ogrenci1.adi)

print(ogrenci1.yasi)
print(ogrenci1.sozluk)
ogrenci1.yasi=20
print(ogrenci1.yasi)
print(ogrenci1.sozluk)
ogrenci1.dogum_tarihi()