'''
dizi=[0,1,2,3,4,5,6,7,8]
dizi1=[5,9,8,1,3,7,0,4,2,6,-1]
ortak=[]

for i in range(len(dizi)):
    for j in range(len(dizi1)):
        try:
            if (dizi.index(i)== dizi1.index(j)):
                ortak.append(dizi.index(i))
                print(j)
            else:
                continue
        except ValueError as hata:
            print("Hata")


print(ortak)

------------------------------------------------------------

a=[0,1,2,3,4,5,6,7,8]
b=[5,9,8,1,3,7,0,4,2,6,-1]

for i in b:
    try:
        if i == a.index(i):
            print("yes")

    except:
        print("no")
        continue
'''