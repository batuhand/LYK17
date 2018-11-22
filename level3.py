a="Bugün 23 Nisan,bu gün türkiye için önemli bir gün. Çocukların stadyumda mutluluk ile parlayan gözleri beni çoK mutlu ediyor. Türkiye'de tüm kalpler\
Atatürk için atıyor.80 milyon insanın kalbi bu bayram için atıyor!"
"""
c=set(a)

print (type(c))
print(c)

print(len(c))
sayilar=["0","1","2","3","4","5","6","7","8","9"]
dizi=[]
for i in range(len(a)):
    for j in range(10):
        if a[i]==sayilar[j]:
            dizi.append(a[i])

print(dizi)
"""

for karakter in a:
    try:
        print(int(karakter))

    except:
        continue