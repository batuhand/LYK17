import random

kelimeler=["kokoreç","midye","sucuk","katmer"]

kelime = random.choice(kelimeler)
print(set(kelime))

can = len(kelime)
bilinen=[]
print(kelime)
a=True
while a==True:
    for i in range(len(kelime)):
        if len(set(kelime))==len(set(bilinen)):
            print("Oyunu kazandınız")
            print(kelime)
            break
            a=False
        a = input("Harf alayım : ")
        if a in bilinen:
            print("Bu harfi zaten girdiniz!")
            continue
        if a.lower() in kelime:
            print("Harf doğru")
            bilinen.append(a)
            print(bilinen)
        else:
            can = can - 1
            print(can,"tane canın kaldı")
            continue
