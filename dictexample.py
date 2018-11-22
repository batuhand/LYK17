data={0:{"ad":"","soyad":"","bolum":"","alınan dersler":"","sınıf":"","numara":"","kaldığı dersler":"","geçtiği dersler":"",\
         "büte girdiği dersler":"","danışman":"","geçtiğidersnot":[],"ortalama":[]},\
      1:{"ad":"","soyad":"","bolum":"","alınan dersler":"","sınıf":"","numara":"","kaldığı dersler":"","geçtiği dersler":"",\
         "büte girdiği dersler":"","danışman":"","geçtiğidersnot":[],"ortalama":[]},\
      2:{"ad":"","soyad":"","bolum":"","alınan dersler":"","sınıf":"","numara":"","kaldığı dersler":"","geçtiği dersler":"",\
         "büte girdiği dersler":"","danışman":"","geçtiğidersnot":[],"ortalama":[]}}

print(data)

print(data[0]["ad"])

ogrSayi=0
gecDers = 0
ortDers=0

while (ogrSayi<3):

    data[ogrSayi]["ad"] = input("Ad :")
    data[ogrSayi]["soyad"] = input("Soyad :")
    data[ogrSayi]["bolum"] = input("Bölüm :")
    data[ogrSayi]["alınan dersler"] = input("Alınan dersler :")
    data[ogrSayi]["sınıf"] = input("Sınıf :")
    data[ogrSayi]["numara"] = input("No :")
    data[ogrSayi]["kaldığı dersler"] = input("Kaldığın dersler : ")
    data[ogrSayi]["geçtiği dersler"] = input("Geçtiğin dersler : ")
    data[ogrSayi]["büte girdiği dersler"] = input("Büte girilen dersler : ")
    data[ogrSayi]["danışman"] = input("Danışmanın : ")
    print("Geçtiğin derslerin notu :")
    input(gecDers)
    data[ogrSayi]["geçtiğidersnot"].append(gecDers)
    print("Geçtiğin derslerin ortalaması :")
    input(ortDers)
    data[ogrSayi]["ortalama"].append(ortDers)
    ogrSayi=ogrSayi+1

print (data[0],data[1],data[2])

ogrOrt=0

ogrOrt = (data[0]["geçtiğidersnot"] + data[1]["geçtiğidersnot"] + data[2]["geçtiğidersnot"])/3

print(ogrOrt)
