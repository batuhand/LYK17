'''
def func(x):
    x=x*x*x-(3*x*x)+x-2
    return x

a=input("x = ")
print(func(int(a)))
'''

sayi1=int(input("Sayi 1 : "))
sayi2=int(input("Sayi 2 : "))

toplama = lambda sayi1,sayi2:sayi1+sayi2

print(toplama(sayi1,sayi2))