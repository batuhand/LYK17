import json
import os

class piton:
    def __init__(self):
        self.sayac = 0
        self.sozluk = {}

    def dict_to_json(self,data):
        return json.dumps(data)

    def json_to_dict(self,data):
        self.sayac = 0
        bos = {}
        try:
            for i in json.loads(data).keys():
                if int(i) > self.sayac:
                    self.sayac = int(i)
            self.sayac +=1
        except:
            return bos
        return json.loads(data)

    def read_file(self,file_path):
        data = None
        if not self.is_non_zero_file(file_path):
            return data
        f = open(file_path,"r")
        data = f.read()
        f.close()
        return data

    def write_file(self,data,file_path):
        with open(file_path,"w") as f:
            f.write(data)

    def add_student(self,sozluk):
        eski_sozluk = {}
        eski_bilgi = self.read_file("bilgiler.json")
        if eski_bilgi:
            eski_sozluk = self.json_to_dict(eski_bilgi)
        eski_sozluk[self.sayac] = sozluk
        yeni_json = self.dict_to_json(eski_sozluk)
        self.write_file(yeni_json,"bilgiler.json")

    def is_non_zero_file(self,fpath):
        if os.path.isfile(fpath) and os.path.getsize(fpath) > 0:
            return True
        return False

    def delete_student(self,index):
        bilgiler1 = self.read_file("bilgiler.json")
        bilgiler = self.json_to_dict(bilgiler1)
        del bilgiler[index]
        print (bilgiler)

    def find_student(self,ad,soyad):
        a = self.read_file("bilgiler.json")
        b = self.json_to_dict(a)
        for i in b.keys():
            if b[i]["adi"] == ad and b[i]["soyadi"] == soyad:
                return i

if __name__ == "__main__":
    hello_world = piton()
    bilgi = {"adi":"irem","soyadi":"ozer","dogum tarihi":94}
    bilgi2 = {"adi":"doğukan","soyadi":"eray","dogum tarihi":97}


    hello_world.add_student(bilgi)
    hello_world.add_student(bilgi2)
    print(hello_world.read_file("bilgiler.json"))

