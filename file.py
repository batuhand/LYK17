'''f = open("deneme.txt")
r = f.readline()

print(r)
print("*" * 10)

r = f.readline()
print(r)
f.close()
'''

with open("deneme.txt","r") as dosya:
    icerik = dosya.readline()

print(icerik)