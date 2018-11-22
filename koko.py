import json

def price():
    json.loads("kokoData.json")
    dosya = open("kokoData.json","r")
    a = dosya.read()
    print (a)
    dosya.close()

def add():
    urunSayi = input("Kaç tane ürün eklemek istiyorsun? : ")
    dosya = open("kokoData.json","a")
    for i in range(urunSayi):
        urun=input("Ürün adı : ")
        fiyat=input("Ürün fiyatı")
        urunler={urun : fiyat}
        dosya.write(urunler)
    dosya.close()

def urunMiktar():
    json.loads("kokoData.json")
    dosya = open("kokoData.json","r")
    a = dosya.read()
    print (a)
    dosya.close()

def siparisListe():
    json.loads("kokoSiparis.json")
    dosya = open("kokoSiparis.json","r")
    a = dosya.read()
    print (a)
    dosya.close()

def userMenu():
    dosya = open("kokoData.json","r")
    json.loads("kokoData.json")
    a = dosya.read()
    print (a)
    siparisler = {}
    sayi=input("Kaç tane ? : ")
    siparis = input("Ne siparişi vereceksin ?\n1)Kokoreç\n2)Midye\n3)Sucuk\n4)İçecek")
    if siparis==1:
        fiyat = int(a["kokoreç"])*sayi
        print(fiyat,"tl tuttu")
        siparisler["kokoreç":sayi]
        yazdir(siparisler)
    if siparis == 2:
        fiyat = int(a["midye"])*sayi
        print(fiyat,"tl tuttu")
        siparisler["midye":sayi]
        yazdir(siparisler)
    if siparis == 3:
        fiyat = int(a["sucuk"])*sayi
        print(fiyat,"tl tuttu")
        siparisler["sucuk":sayi]
        yazdir(siparisler)
    if siparis == 4:
        fiyat = int(a["içecek"])*sayi
        print(fiyat,"tl tuttu")
        siparisler["içecek":sayi]
        yazdir(siparisler)
    dosya.close()

def yazdir(a):
    dosya = open("kokoSiparis.json","a")
    b = json.dumps(a)
    dosya.write(b)
    dosya.close()

def resMenu():
    check=input("1)Ürün fiyatlarını gör\n2)Ürün ekle\n3)Ürün stok miktarı\n/"
                "4)Ürün silme\n5)Sipariş listesi")
    if check == 1:
        price()
    if check == 2:
        add()
    if check == 3:
        urunMiktar()
    if check == 5:
        siparisListe()

def fisVer():
    dosya=open("kokoSiparis.json","r")
    json.loads(dosya)
    a = dosya.read()
    print(a)


open=input("1)Kullanıcı girişi\n2)Restoran girişi\nSeçim : ")

if open==1:
    userMenu()
if open==2:
    resMenu()
