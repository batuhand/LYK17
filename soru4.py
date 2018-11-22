girilenVeri=[]
karakterSayi=[]
dogru=[]
sonuc={}


def veriAl(girdi):
    if girdi.isdigit():
        print("HATA!")
    else:
        girilenVeri.append(girdi)
        return 0

def karakterSayisi(b):
    print(girilenVeri)
    for i in range(b):
        a = len(girilenVeri[i])
        karakterSayi.append(a)


def boolKontrol(dizi):
    for i in range(veriSayi):
        if (int(dizi[i])%2==0):
            dogru.append(True)
        else:
            dogru.append(False)

def sozlukYaz(a,b,c):
    for i in range(veriSayi):
        sonuc = {a[i]: (b[i], c[i])}
        print(sonuc)

veriSayi = int(input("Kaç tane veri girilsin : "))
for i in range(veriSayi):
    veri=input("Kelimeleri girin :")
    veriAl(veri)
    print(veriSayi)
karakterSayisi(veriSayi)
boolKontrol(karakterSayi)
sozlukYaz(girilenVeri,karakterSayi,dogru)

