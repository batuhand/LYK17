'''
def yazdir(deger1,deger2):
    print(deger1,deger2)


yazdir(deger1="yaz",deger2="kampı")
yazdir(deger2="kampı",deger1="yaz")
yazdir("yaz","kampı")
yazdir("kampı","yaz")
anahtar1="yaz"
anahtar2="kampı"

yazdir(anahtar1,anahtar2)
yazdir(anahtar2,anahtar1)
'''

def bilgiler(ad,soyad,yas=None):
    print("Adı: ",ad)
    print("Soyadı: ",soyad)
    print("Yaşı",yas)
    print("-"*10)

bilgiler("hakan","yıldız",24)
bilgiler("Özge","Barbaros")
