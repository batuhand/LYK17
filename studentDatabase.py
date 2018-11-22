import json
kayitSayi=1
girisAdi=""
girisParola=""
data={kayitSayi:{"kullaniciadi":"","parola":"","ad":"","soyad":"","okul":"","bolum":""}}

girisKontrol=int(input("1) Giriş Yap\
                   2) Kayıt ol"))
if girisKontrol==2:
    data[kayitSayi]["kullaniciadi"]=input("Kullanıcı adı giriniz : ")
    data[kayitSayi]["parola"]=input("Parolanızı giriniz : ")
    data[kayitSayi]["ad"]=input("Ad : ")
    data[kayitSayi]["soyad"]=input("Soyad : ")
    data[kayitSayi]["okul"]=input("Okul : ")
    data[kayitSayi]["bolum"]=input("Bölüm : ")
    girisVeri=json.dumps(data)
    dosya = open("stData.txt","a")
    dosya.write(girisVeri)
    kayitSayi=kayitSayi+1
    print("Kaydınız yapıldı.")

if girisKontrol==1:
    dosya = open("stData.json","r")
    girisYap=json.dumps(data)
    girisYap=json.loads(str(data))
    girisAdi=input("Kullanıcı adınızı girin : ")
    for i in range(1,kayitSayi):
        if (girisYap[i]["kullaniciadi"] == girisAdi):
            girisParola=input("Parolanızı girin : ")
            for j in range(1,kayitSayi):
                if (girisYap[i]["parola"]== girisParola):
                    print("Başarıyla giriş yaptınız!")
                else:
                    print("Giriş başarısız!")
        else:
            print("Giriş başarısız!")
else:
    print("Geçersiz giriş")







