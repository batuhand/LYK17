from jsontekrar import piton
ogrenci = piton()
def ogrenciListele():
    a = ogrenci.read_file("bilgiler.json")
    b = ogrenci.json_to_dict(a)
    print(b)

def ogrenciEkle(sozluk):
    ogrenci.add_student(sozluk)

def ogrenciSil(a):
    ogrenci.delete_student(a)
    print("A T I L D I N")

def ogrenciBul(ad,soyad):
    index = ogrenci.find_student(ad,soyad)
    a = ogrenci.read_file("bilgiler.json")
    b = ogrenci.json_to_dict(a)
    print (b[index])


def menu():
    while True:
        secim =int(input("1)Öğrencileri listele\n2)Öğrenci ekle\n3)Öğrenci sil\n4)Öğrenci bul\n5)Çıkış\nSeçim :"))
        try:
            int(secim)
        except:
            print("Geçerli bir değer girin! ")
            continue

        if secim == 1:
            ogrenciListele()

        if secim == 2:
            ad = input("Öğrenci adını girin :")
            soyad = input("Öğrenci soyadını girin : ")
            tarih = input("Doğum tarihini girin : ")
            sozluk = {"adi": ad,"soyadi":soyad,"dogum tarihi":tarih}
            ogrenciEkle(sozluk)

        if secim == 3:
            ogrenci.read_file("bilgiler.json")
            a = input("Hangi indexteki öğrenciyi silmek istiyorsun : ")
            ogrenciSil(a)

        if secim == 4:
            adi = input("Öğrenci adı girin : ")
            soyadi = input("Öğrenci soyadını girin : ")
            ogrenciBul(adi,soyadi)

        if secim == 5:
            break
            return 0

menu()