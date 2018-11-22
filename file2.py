'''
a=input("Yazı yaz : ")
dosya=open("dosya.txt","w")
sonuc = dosya.write(a)
sonuc1=dosya.close()
print("sonuç ",sonuc)
print("sonuç1",sonuc1)

dosya=open("dosya.txt","r")
icerik=dosya.read()
print(icerik)
'''
import json

def veri_al():
    a=input("Selam Python")
    return {"python":a}

def dosya_oku(dosya_yolu):
    dosya=open(dosya_yolu,"r")
    icerik = dosya.read()
    dosya.close()
    return json.loads(icerik)

def dosyaya_yaz(dosya_tum_yolu,icerik):
    yeni_icerik=json.dumps(icerik)
    dosya=open(dosya_tum_yolu,"w")
    dosya.write(yeni_icerik)
    dosya.close()

veri=veri_al()
dosyaya_yaz("python.json",veri)
check=dosya_oku("python.json")
print(check)
print(dosya_oku("python.json"))
ikinci_veri = veri_al()
ikinci_dosya_okuma = dosya_oku()