fact1 = int(input("Faktöriyeli alınacak sayıyı girin"))
'''
carp=1

if(fact==1 or fact==0):
    print(carp)

else:
    for i in range(fact):
        carp=carp*(i+1)


    print(carp)
'''


def fact(c):
    if c== 0:
        return 1

    else:
        return c*(fact(c-1))

print(fact(int(fact1)))