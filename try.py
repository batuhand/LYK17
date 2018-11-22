'''
try:
    print(x)

except:
    print("üzgünüm x değişkeni tanımlı değil!")

-------------------------
try:
    yas = int(input("Yaşın kaç?"))
    print(yas)

except ValueError as hata:
    print(hata.args[0])
    print("Tip hatası")

print("lyk")

'''

for i in ["5",(5,4),9,"m","6"]:
    try:
        print(int(i)*2)
    except TypeError as hata1:
        print("Tip hatası : ",hata1)
    except ValueError as hata2:
        print("Değer Hatası ",hata2)
