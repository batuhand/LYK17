class Album():
    def __init__(self,isim,sanatci,turu):
        self.adi = isim
        self.tur = turu
        self.sanatci = sanatci
        self.sarkilar = []

    def sarkiGuncelle(self,yeniSarki):
        self.sarkilar.append(yeniSarki)
        print(yeniSarki)

    def sarkiListele(self):
        for i in self.sarkilar:
            print(i.adi,i.sanatci,i.tur)

class Sarki():
    def __init__(self,isim,sanatci,tur):
        self.adi = isim
        self.sanatci = sanatci
        self.tur = tur



gibi_gibi = Sarki("Gibi Gibi","Mehmet E","Pop")

yeni_album = Album("Hiç k.","Mehmet Erdem","Pop")
yeni_album.sarkiGuncelle(gibi_gibi)
yeni_album.sarkiListele()