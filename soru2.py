sayi1=input("Birinci sayiyi gir:")
sayi2=input("İkinci sayiyi gir:")
dizi=[]
def ortakBol(a,b):
    if (a>b):
        for j in range(1,int(a)):
            if(int(a)%j==0 and int(b)%j==0):
                dizi.append(j)

    if(b>a):
        for k in range(1,int(b)):
            if(int(b)%k==0 and int(a)%k==0):
                dizi.append(k)

    else:
        dizi.append(a)

ortakBol(sayi1,sayi2)
print(dizi)