hava = 0

print("Yağmur yağıyor mu?\n1)Yağmur yağıyor\n2)Yağdı yağacak\n3)Yağmıyor")
hava=input()

hava = int(hava)

if hava==1:
    print("Yanına şemsiye al!")

elif hava==2:
    print("Sen yine de al")

elif hava==3:
    print("Şemsiye almasan da olur")

else:
    print("Geçerli bir değer girmedin ama")