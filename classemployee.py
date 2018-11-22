class Calisan:
    def __init__(self,isim,maas,departman):
        self.ad = isim
        self.ucret = maas
        self.bolum = departman

    def bilgiBas(self):
        print(10*"-","\nPersonel adı :",self.ad,"\nAldığı maaş :",self.ucret,"\nBölümü : ",self.bolum)

    def maasZammi(self,zam):
        print("Eski maaşı :",self.ucret)
        self.ucret = self.ucret + zam
        print("Yeni maaş :",self.ucret)

    def departmanGuncelle(self,yeniBolum):
        print("Çalışan :",self.ad,"\nEski bölüm : ",self.bolum)
        self.bolum = yeniBolum
        print("Yeni bölüm : ",self.bolum)


class Yonetici(Calisan):
    def __init__(self,calisan,ad,ucret,bolum):
        self.altCalisan = []
        super(Yonetici, self).__init__(ad,ucret,bolum)

    def bilgiBas(self):
        print(10*"-","\nPersonel adı :",self.ad,"\nAldığı maaş :",self.ucret,"\nBölümü : ",self.bolum)

    def altCalisan_ekle(self,calisan):
        self.altCalisan.append(calisan)

    def altCalisan_yazdir(self):
        for i in self.altCalisan:
            print(i.ad,i.ucret,i.bolum)

ahmet = Calisan("Ahmet",3,"Yok")

ahmet.bilgiBas()

mehmet = Yonetici("15","Mehmet",50,"Yonetici")
mehmet.bilgiBas()

ahmet.maasZammi(2)

a= input("Ahmetin yeni bölümü ne olsun ? : ")
ahmet.departmanGuncelle(a)

mehmet.maasZammi(5)

ekleSayi = int(input("Kaç tane alt çalışan eklemek istiyorsun : "))

for i in range(ekleSayi):
    isim = input("Eklenecek çalışanın adı : ")
    maas = input("Çalışanın maaşı : ")
    dep = input("Çalışanın departmanı :")
    j = Calisan(isim,maas,dep)
    mehmet.altCalisan_ekle(j)

mehmet.altCalisan_yazdir()

