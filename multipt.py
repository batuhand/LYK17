'''
import time
a=time.time()
kaca_kadar = 500000
def asal(kaca_kadar):

    asallar = [2]
    if kaca_kadar < 2:
        return None
    elif kaca_kadar == 2:
        return asallar
    else:
        for i in range(3,kaca_kadar,2):
            bolundu = False
            limit = (i ** 0.5) + 1
            for j in asallar:

                if i % j == 0:
                    bolundu=True
                    break
                if j > limit:
                    break
            if bolundu == False:
                asallar.append(i)
    return asallar

b = time.time()
print(asal(kaca_kadar))
print(b-a)
print(len(asal(kaca_kadar)))

a = asal(kaca_kadar)
for i in range(1,len(a)):
    a[i] = a[i]+a[i-1]

print (a[41537])
'''
import time
import math
from multiprocessing import Pool


def asal_mi(sayi):
    if sayi<2:
        return False
    if sayi%2==0:
        return False
    bolunecekler = range(3,int(math.sqrt(sayi))+1,2)
    for x in bolunecekler:
        if sayi%x == 0:
            return False
    return True

def sayilar_asal_mi(sayilar):
    return [x for x in sayilar if asal_mi(x)]

if __name__=="__main__":
    p = Pool(processes=4)
    eski = time.time()
    sonuclar = p.map(sayilar_asal_mi,[range(2,62500),range(62500,125000),range(125000,187500),range(187500,250000),range(250000,312500),range(312500,375000),range(375000,437500),range(437500,500000)])
    print(time.time()-eski)
    print(sonuclar)
    alt_toplamlar = map(sum,sonuclar)
    print(alt_toplamlar)
    print(sum(alt_toplamlar))
