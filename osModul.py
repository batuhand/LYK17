'''
import os

def sil(yol):
    os.system("cd ",yol)
    a = os.system("ls")
    for i in a:
        os.remove(i)

    os.rmdir(yol)

print(os.system("ls"))



dosyaYolu=input("Neredeki dosyayı silmek istiyorsun : ")
sil(dosyaYolu)

'''

import os

dizinAl=input("dizin gir : ")
icindeki=os.listdir(dizinAl)

for dosya in icindeki:
    os.remove(dizinAl+dosya)
os.rmdir(dizinAl)

#os.path.join(dizinAl,dosya)
