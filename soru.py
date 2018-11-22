def func(ogrSayi,bilgi):

    for i in range(1, ogrSayi):
        data1 = {ogrSayi: bilgi}
        print(data1)

sayi = 1
data={"ad":"","soyad":"","bolum":"","okul":""}

while(sayi<=2):
    data["ad"] = input("Ad :")
    data["soyad"] = input("Soyad :")
    data["bolum"] = input("Bölüm :")
    data["okul"] = input("Okul :")
    if (sayi==2):
        break
    sayi = sayi+1

func(sayi,data)