class Canli():
    def __init__(self,solunum,ureme,bosaltim,sindirim):
        self.solunum = solunum
        self.ureme = ureme
        self.bosaltim = bosaltim
        self.sindirim = sindirim


class Hayvan(Canli):
    def __init__(self,solunum,ureme,bosaltim,sindirim,ayaksayi,yasamyeri):
        self.ayaksayi = ayaksayi
        self.yasamyeri = yasamyeri
        super().__init__(solunum,ureme,bosaltim,sindirim)

class Bitki(Canli):
    def __init__(self,solunum,ureme,bosaltim,sindirim,meyve,yasamyeri,kok):
        self.meyve = meyve
        self.yasamyeri = yasamyeri
        self.kok = kok
        super().__init__(solunum,ureme,bosaltim,sindirim)

class Sumbul(Bitki):
    def __init__(self,solunum,ureme,bosaltim,sindirim,meyve,yasamyeri,kok,renk):
        self.renk = renk
        super().__init__(solunum,ureme,bosaltim,sindirim,meyve,yasamyeri,kok)

    def yazdir(self):
        print("Bu sümbülün solunumu", self.solunum, "üreme tipi", self.ureme, "boşaltım tipi", self.bosaltim,"sindirimi",self.sindirim, \
              "meyvesi",self.meyve,"yaşam yeri", self.yasamyeri,"kökleri",self.kok,"rengi",self.renk)


class Okuz(Hayvan):
    def __init__(self,solunum,ureme,bosaltim,sindirim,ayaksayi,yasamyeri,kilo,kafaturu):
        self.kilo = kilo
        self.kafaturu = kafaturu
        super().__init__(solunum,ureme,bosaltim,sindirim,ayaksayi,yasamyeri)

    def yazdir(self):
        print("Bu öküzün solunumu", self.solunum, "üreme tipi", self.ureme, "boşaltım tipi", self.bosaltim,"ayak sayisi", \
              self.ayaksayi,"sindirimi",self.sindirim, "yaşam yeri", self.yasamyeri, "kilosu",self.kilo,"kafa türü", self.kafaturu)


class Baykus(Hayvan):
    def __init__(self,solunum,ureme,bosaltim,sindirim,ayaksayi,yasamyeri,kafaturu,derece):
        self.kafaturu = kafaturu
        self.derece = derece
        super().__init__(solunum,ureme,bosaltim,sindirim,ayaksayi,yasamyeri)

    def yazdir(self):
        print("Bu baykuşun solunumu",self.solunum,"üreme tipi",self.ureme,"boşaltım tipi",self.bosaltim,"ayak sayisi",\
              self.ayaksayi,"sindirimi",self.sindirim,"yaşam yeri",self.yasamyeri,"kafa türü",self.kafaturu,"dönme derecesi",self.derece)


a = Sumbul("fotosentez","sporla","damlama","sade soda","çiçek","dünya","var","mor")
a.yazdir()

b = Okuz("burun","bambambam","dışkı","mide","4","köyler","800","büyük")
b.yazdir()

c = Baykus("burun","yumurta","var","mide","2","ağaçlar","döner başlı","360")
c.yazdir()