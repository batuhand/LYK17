'''

def yazilim(ad,soyad,yas,cinsiyet):
    return(ad,soyad,yas,cinsiyet)


degerler=yazilim("metin","ataş",30,"erkek")
print(degerler)
print(degerler[0])
print(degerler[1])
print(type(degerler))

#tuple dönrürür
'''
'''
def yazilim(ad,soyad,yas,cinsiyet):
    bilgiler=[ad,soyad,yas,cinsiyet]
    return(bilgiler)

degerler=yazilim("metin","ataş",30,"erkek")
print(degerler)
print(degerler[0])
print(degerler[1])
print(degerler[2])
print(degerler[3])
print(type(degerler))
#list döndürür
'''

def yazilim(ad,soyad,yas,cinsiyet):
    bilgiler={"ad":ad,"soyad":soyad,"yas":yas,"cinsiyet":cinsiyet}
    return(bilgiler)

degerler=yazilim("metin","ataş",30,"erkek")
print(degerler)
print(degerler.keys())
print(degerler["ad"])
print(degerler["soyad"])
print(type(degerler))