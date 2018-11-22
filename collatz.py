"""
n=int(input("n sayısını girin : "))
a=True
while (a==True):
    if n==1:
        a=False
    if (n%2==0):
            print(n)
            n=n/2
    else:
        print(n)
        n=3*n+1


"""
def sonuc(n):
    if(n%2==0):
        print(n//2)
        return sonuc(n//2)
    elif(n==1):
        print(n)
        return 0
    else:
        print(3*n+1)
        return sonuc(3*n+1)


a=int(input("n sayisi : "))
sonuc(a)