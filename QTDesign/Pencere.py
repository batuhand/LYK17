import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
import os
import json

class AnaPencere(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"ui/main.ui")
        loadUi(ui_path,self)
        self.kaydetButon.clicked.connect(self.butonaTiklandi)
        self.dosya_ismi = "kisiler.json"
        self.kisiListele()


    def kisiListele(self):
        self.liste.clearContents()
        self.liste.setHorizontalHeaderLabels(["İsim","Soyisim","Telefon"])
        self.liste.setColumnCount(3)
        try:
            kisiler = json.load(open(self.dosya_ismi, "r"))
        except:
            kisiler = []
        row_count = len(kisiler)
        self.liste.setRowCount(row_count)
        row_no = 0
        for kisi in kisiler:
            ad = QTableWidgetItem(kisi.get("ad"))
            soyad = QTableWidgetItem(kisi.get("soyad"))
            telefon = QTableWidgetItem(kisi.get("telefon"))
            self.liste.setItem(row_no,0,ad)
            self.liste.setItem(row_no,1,soyad)
            self.liste.setItem(row_no,2,telefon)
            row_no +=1


    def butonaTiklandi(self):
        print(self.ad.text())
        print("Tiklandi")
        try:
            kisiler = json.load(open(self.dosya_ismi,"r"))
        except:
            kisiler = []
        kisi = {"isim":self.ad.text(),"soyisim":self.soyad.text(),"telefon":self.telefon.text()}
        kisiler.append(kisi)
        open(self.dosya_ismi,"w+").write(json.dumps(kisiler))

if __name__== '__main__':
    app = QApplication([])
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec())
