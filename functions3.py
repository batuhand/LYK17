def insanlarin_ozellikleri(ad,soyad,*ozellikler):

    print("Adı :",ad)
    print("Soyadı :",soyad)

    ozellikleri=""
    for ozellik in ozellikler:
        ozellikleri = ozellikleri + " " + ozellik
    print ("Özellikleri :",ozellikleri)
    print("-"*5)

insanlarin_ozellikleri("Hakan","Yıldız","esmer","siyah saçlı","uzun boylu","python sever") #tuple
