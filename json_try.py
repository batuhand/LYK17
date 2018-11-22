import json

sozluk = {0:{"ad":"","soyad":""}}


with open("jsonDeneme.json","a+") as dosya:
    a= json.dumps(sozluk)
    dosya.write(a)

