'''
import random

kontrol = random.randrange(1,3)

if kontrol == 1:
    oyuncu1 = "X"
    oyuncu2 = "O"

if kontrol == 2:
    oyuncu1 = "O"
    oyuncu2 = "X"

print("1. Oyuncu : ",oyuncu1)
print("2. Oyuncu : ",oyuncu2)


saha = ["1","2","3","4","5","6","7","8","9"]

for i in range(9):
    if i%3==2:
        print (saha[i-2],saha[i-1],saha[i])

while True:
    a = int(input("1. Oyuncu nereyi çizeceksin : "))
    saha[a-1] = oyuncu1
    for i in range(9):
        if i % 3 == 2:
            print(saha[i - 2], saha[i - 1], saha[i])
    if (saha[0] == saha[1] == saha[2] == oyuncu1 or saha[3] == saha[4] == saha[5] == oyuncu1 or saha[6] == saha[7] == saha[8] == oyuncu1 or\
            saha[0] == saha[3] == saha[6] == oyuncu1 or saha[1] == saha[4] == saha[7] == oyuncu1 or saha[2] == saha[5] == saha[8]== oyuncu1):
        print("1. Oyuncu kazandı !")
        break
    b = int(input("2. Oyuncu nereyi çizeceksin : "))
    saha[b-1] = oyuncu2
    for i in range(9):
        if i % 3 == 2:
            print(saha[i - 2], saha[i - 1], saha[i])
    if (saha[0] == saha[1] == saha[2] == oyuncu2 or saha[3] == saha[4] == saha[5] == oyuncu2 or saha[6] == saha[7] == saha[8] == oyuncu2 or\
            saha[0] == saha[3] == saha[6] == oyuncu2 or saha[1] == saha[4] == saha[7] == oyuncu2 or saha[2] == saha[5] == saha[8]== oyuncu2):
        print("2. Oyuncu kazandı !")
        break

'''

tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

print("\n"*15)

for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)

kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]

x_durumu = []
o_durumu = []

sıra = 1
while True:
    if sıra % 2 == 0:
        işaret = "X".center(3)
    else:
        işaret = "O".center(3)

    print()
    print("İŞARET: {}\n".format(işaret))
    try:
        x = int(input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30)))
        if(x<1 or x>3):
            print("Geçerli değer gir!")
            continue
        if x == "q":
            break
        y = int(input("soldan sağa [1, 2, 3]: ".ljust(30)))
        if (y < 1 or y > 3):
            print("Geçerli değer gir!")
            continue
        if y == "q":
            break
    except:
        print("Harf giremezsin !")
        continue
    x = x-1
    y = y-1

    print("\n"*15)

    if tahta[x][y] == "___":
        tahta[x][y] = işaret
        if işaret == "X".center(3):
            x_durumu += [[x, y]]
        elif işaret == "O".center(3):
            o_durumu += [[x, y]]
        sıra += 1
    else:
        print("\nORASI DOLU! TEKRAR DENEYİN\n")

    for i in tahta:
         print("\t".expandtabs(30), *i, end="\n"*2)

    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        if len(o) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit()
    if len(x_durumu) + len(o_durumu) == 9:
        print("oyun bitti")
        quit()


