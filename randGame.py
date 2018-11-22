import random


sayi = random.randrange(5)
tahminSayi = 0
print(sayi)


while True:
    tahmin = int(input("Tahmin et (0'la 100 arasında) : "))
    tahminSayi = tahminSayi + 1
    if sayi == tahmin:
        print(tahminSayi, "tahminde buldunuz!")
        break
    elif (sayi>tahmin):
        print("Biraz daha yukarı !")
    elif (tahmin>sayi):
        print("Biraz aşağı !")