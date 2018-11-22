'''
def sa():
    print("Batuhan")
    print("Demircan")
    print("20")


sa()
'''

def carp(a,b):
    c=a*b
    return c

def bol(d,e):
    f=d/e
    return f



sec = input("Çarpma için 1'e bölme için 2'ye basın")
sayi1 = input("Birinci sayiyi girin")
sayi2 = input("İkinci sayiyi girin")

if sec == 1:
    sonuc = carp(int(sayi1),int(sayi2))
    print(sonuc)
if sec == 2:
    sonuc = bol(int(sayi1),int(sayi2))
    print(sonuc)

