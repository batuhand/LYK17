sesli=["a","e","ı","i","o","ö","u","ü","A","E","ı","I","O","Ö","U","Ü"]
sacma=[".",","," ","1","2","3","4","5","6","7","8","9","10"]

cumle = "bugün 2. evimi aldım. yavaş yavaş sadece kira gelirleriyle geçinen insan olmaya doğru ilerliyorum 10 yıl civarında 3 ev daha almayı planlıyorum. şu an aylık 300 dolar kira gelirim var aslında aylık 500 dolar yeter bana o zaman her şeyi geride bırakıp bu ülkeden paket olup gideceğim rahat rahat. çünkü 500 dolar bana yaşamak için yeter de artar."

sesliHarf=0
sessizHarf=0
harfSayi=0
sacmaHarf = 0

for i in cumle:
    harfSayi=harfSayi+1
    if i in sesli:
        sesliHarf=sesliHarf+1
    if i in sacma:
        sacmaHarf = sacmaHarf+1

print(harfSayi)

sessizHarf=harfSayi-sesliHarf-sacmaHarf

print(sesliHarf,sessizHarf)
