class insanlar():
    def __init__(self,mevki = "isci",saldirigucu=50,savunmagucu=10,kalancan=120):
        self.mevki = mevki
        self.saldirigucu = saldirigucu
        self.savunmagucu = savunmagucu
        self.kalancan = kalancan

    def durum(self):
        print("Bu insan bir ",self.mevki,". Saldırı gücü : ",self.saldirigucu,"Savunma gücü :",self.savunmagucu,"Kalan canı ise : ",self.kalancan)

    def saldir(self):
        print(self.mevki, "bir saldırı başlattı !")

class hero(insanlar):
    def __init__(self,orduKur,mevki,saldirigucu,savunmagucu,kalancan):
        self.orduKur = orduKur
        super().__init__(mevki,saldirigucu,savunmagucu,kalancan)


    def durum(self):
        print("Bu hero ", self.mevki, ". Saldırı gücü : ", self.saldirigucu, "Savunma gücü :", self.savunmagucu,"Kalan canı ise : ", self.kalancan,"Ordu kurma gücü : ",self.orduKur)



okcu = insanlar("okçu",150,120,200)
atlı = insanlar("atlı",200,100,150)
arkantos = hero("Arkantos","tanrı",300,500,1500)
isci = insanlar()

arkantos.durum()
okcu.durum()
atlı.durum()
isci.durum()