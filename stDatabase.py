'''
import json
def register():
    data = {"kullaniciadi": "", "parola": "", "ad": "", "soyad": "", "okul": "", "bolum": ""}
    data["kullaniciadi"] = input("Kullanıcı adı giriniz : ")
    data["kullaniciadi"]["parola"] = input("Parolanızı giriniz : ")
    data["kullaniciadi"]["ad"] = input("Ad : ")
    data["kullaniciadi"]["soyad"] = input("Soyad : ")
    data["kullaniciadi"]["okul"] = input("Okul : ")
    data["kullaniciadi"]["bolum"] = input("Bölüm : ")
    girisVeri = json.dumps(data)
    dosya = open("stData.json", "a")
    dosya.write(girisVeri)
    print("Kaydınız yapıldı.")

def signIn():
    with open("stData.json") as json:
        json.read(500)
        girisYap = json.load(json)

    girisAdi = input("Kullanıcı adınızı girin : ")
    for i in range(1,10):
        if (girisYap["kullaniciadi"] == girisAdi):
            girisParola = input("Parolanızı girin : ")
            for j in range(1,10):
                if (girisYap["kullaniciadi"]["parola"] == girisParola):
                    print("Başarıyla giriş yaptınız!")
                    return 1
                else:
                    print("Giriş başarısız!")
                    return 0
        else:
            print("Giriş başarısız!")
            return 0

check=signIn()
if check==1:
    print("1)Aldığın dersleri gör")
    print("2)Aldığın derslerin notlarını gör")
    print("3)Ders ekle")
    print("4)Ders sil")
    control=input("5)Ders notu güncelle")

    if control==3:
        input=(data["kullaniciadi"]["alinandersler"].append)

    if control==1:
        print(data["kullaniciadi"]["alinandersler"])

    if control==5:
        input=(data["kullaniciadi"]["dersnotlari"].append)

    if control==2:
        print(data["kullaniciadi"]["dersnotlari"])
'''
import json


def veri_al():
    a = input()
    return a


def dosya_oku(dosya_yolu):
    dosya = open(dosya_yolu, "r")
    icerik = dosya.read()
    dosya.close()
    return json.loads(icerik)


def dosyaya_yaz(dosya_tum_yolu, icerik):
    yeni_icerik = json.dumps(icerik)
    dosya = open(dosya_tum_yolu, "w")
    dosya.write(yeni_icerik)
    dosya.close()

def kullaniciadi_kontrol(girisAdi):
    for i in range(1,10):
        if data[i]["kullaniciadi"]==girisAdi:
            return 1

def parola_kontrol(girisParola):
    for i in range(1,10):
        if data[i]["parola"]==girisParola:
            return 1

'''
veri = veri_al()
dosyaya_yaz("stData.json", veri)
check = dosya_oku("stData.json")
print(check)
print(dosya_oku("stData.json"))
'''
dosya = open("stData.json", "r")
icerik = dosya.read()
data = json.loads(icerik)

check=input("1)Giriş 2)Kayıt ol")
if check == 1:
    print("Kullanıcı adı girin : ")
    girisAdi = veri_al()
    kontrol1 = kullaniciadi_kontrol(girisAdi)
    if kontrol1==1:
        print("Parola girin : ")
        girisParola = veri_al()
        kontrol2= parola_kontrol(girisParola)

if check == 2:

