ad={}
yas={}
okul={}
bolum={}
kullaniciSayi=0
devam = 1

while(devam ==1):

    while(kullaniciSayi<=10):

        ad[kullaniciSayi]=input("Adınızı girin:")
        yas[kullaniciSayi]=input("Yaşınızı girin:")
        if (yas<18 or yas>60):
            print("Yaşın tutmuyor!")
            continue
        okul[kullaniciSayi]=input("Okulunuzu girin:")
        bolum[kullaniciSayi]=input("Bölümünüzü girin:")
        kullaniciSayi = kullaniciSayi + 1

    if kullaniciSayi==10:
        devam = 0


print(ad,yas,okul,bolum)
