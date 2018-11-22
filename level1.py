try:
    sayi1 = int(input("1. Sayıyı gir : "))
    sayi2 = int(input("2. Sayıyı gir : "))
    print(sayi1/sayi2)

except ValueError as hata:
    print("Lütfen sayı girin")