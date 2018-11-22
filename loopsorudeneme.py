ad=[]
yas=[]
okul=[]
bolum=[]
kullaniciSayi=0
devam = 1

while(devam ==1):

    while(kullaniciSayi<=10):

        ad=input("Adınızı girin:")
        yas=input("Yaşınızı girin:")
        if (int(yas)<18 or int(yas)>60):
            print("Yaşın tutmuyor!")
            continue
        okul=input("Okulunuzu girin:")
        bolum=input("Bölümünüzü girin:")
        kullaniciSayi = kullaniciSayi + 1

    if kullaniciSayi==10:
        devam = 0


print(ad,yas,okul,bolum)
