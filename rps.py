secim1 = input("1. Oyuncu\n1)Taş\n2)Kağıt\n3)Makas")
secim2 = input("2.Oyuncu\n1)Taş\n2)Kağıt\n3)Makas")

if (secim1 == 1 and secim2 == 1):
    print("Berabere!")

if (secim1 == 1 and secim2 == 2):
    print("2. Oyuncu kazandı!")

if (secim1 == 1 and secim2 == 3):
    print("1. Oyuncu kazandı!")

if (secim1 == 2 and secim2 == 1):
    print("1. Oyuncu kazandı!")

if (secim1 == 2 and secim2 == 2):
    print("Berabere!")

if (secim1 == 2 and secim2 == 3):
    print("2. Oyuncu kazandı!")

if (secim1 == 3 and secim2 == 1):
    print("2. Oyuncu kazandı!")

if (secim1 == 3 and secim2 == 2):
    print("1. Oyuncu kazandı!")

if (secim1 == 3 and secim2 == 3):
    print("Berabere!")