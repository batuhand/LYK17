class Futbolcu():
    def __init__(self,ad,soyad,yas,boy,mevkisi,maasi):
        self.adi = ad
        self.soyadi = soyad
        self.yasi = yas
        self.boyu = boy
        self.mevki = mevkisi
        self.maas = maasi
    def maasGuncelle(self,oyuncu,yeniMaas):
        print("Eski maaş ",oyuncu.maas)
        self.maas = yeniMaas
        print(yeniMaas)
'''
print("Takımını seç mücadeleye ortak ol!")

oyuncu1 = Futbolcu()
oyuncu1.adi = "Volkan"
oyuncu1.soyadi = "Demirel"
oyuncu1.yasi = "32"
oyuncu1.boyu = "1.92"
oyuncu1.mevki = "Kaleci"
oyuncu1.maas = "5.000"

oyuncu2 = Futbolcu()
oyuncu2.adi = "Hasan Ali"
oyuncu2.soyadi = "Kaldırım"
oyuncu2.yasi = "29"
oyuncu2.boyu = "1.78"
oyuncu2.mevki = "Sol bek"
oyuncu2.maas = "Aylık dolu akbil"

oyuncu3 = Futbolcu()
oyuncu3.adi = "Simon"
oyuncu3.soyadi = "Kjaer"
oyuncu3.yasi = "27"
oyuncu3.boyu = "1.82"
oyuncu3.mevki = "Stoper"
oyuncu3.maas = "15.000"

oyuncu4 = Futbolcu()
oyuncu4.adi = "Martin"
oyuncu4.soyadi = "Skrtel"
oyuncu4.yasi = "31"
oyuncu4.boyu = "1.86"
oyuncu4.mevki = "Terminatör"
oyuncu4.maas = "10.000"

oyuncu5 = Futbolcu()
oyuncu5.adi = "Şener"
oyuncu5.soyadi = "Özbayraklı"
oyuncu5.yasi = "29"
oyuncu5.boyu = "1.70"
oyuncu5.mevki = "Sağ bek"
oyuncu5.maas = "2.000"

oyuncu6 = Futbolcu()
oyuncu6.adi = "Robin"
oyuncu6.soyadi = "van Persie"
oyuncu6.yasi = "32"
oyuncu6.boyu = "1.80"
oyuncu6.mevki = "Delici Forvet"
oyuncu6.maas = "Kolum bacağım"





hangisi = int(input("Hangi oyuncunun maaşını güncellemek istiyorsun"))
if hangisi == 1:
    maas = input("Yeni maaş :")
    oyuncu1.maasGuncelle(oyuncu1,maas)
if hangisi == 2:
    maas = input("Yeni maaş :")
    oyuncu2.maasGuncelle(oyuncu2,maas)
if hangisi == 6:
    maas = input("Yeni maaş :")
    oyuncu6.maasGuncelle(oyuncu6,maas)

'''


'''

for i in range(11):
    ad = input("Oyuncu ismi gir :")
    oyuncu = Futbolcu()
    oyuncu.adi = ad
    soyad = input("Oyuncu soyadı gir : ")
    oyuncu.soyadi = soyad
    yas = input("Oyuncunun yaşı? : ")
    oyuncu.yasi = yas
    boy = input("Oyuncunun boyu? : ")
    oyuncu.boyu = boy
    mevkisi = input("Oyuncunun mevkisi :")
    oyuncu.mevki = mevkisi
    maasi = input("Oyuncunun MAAŞI????? :")
    oyuncu.maas = maasi
    print(oyuncu.toplam)
'''