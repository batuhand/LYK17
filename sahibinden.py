otomobiller = []
motosikletler = []
kamyonlar = []

class Arac:
    def __init__(self,yil,yer,marka,vites,renk,durum):
        self.uretimYili = yil
        self.uretimYeri = yer
        self.marka = marka
        self.vitesTuru = vites
        self.renk = renk
        self.durum = durum

class Otomobil(Arac):
    def __init__(self,sayi,motorh,yakit,emisyon,klima,ortyakit,km,lastikcap,model,kasatip,ekstra,uretimYili,uretimYeri,marka,vitesTuru,renk,durum):
        self.kapiSayi = sayi
        self.motorHacmi = motorh
        self.yakitTuru = yakit
        self.emisyon = emisyon
        self.klima = klima
        self.ortYakit = ortyakit
        self.kiloMetre = km
        self.lastikCapi = lastikcap
        self.model = model
        self.kasaTipi = kasatip
        self.ekstraOzellik = ekstra
        super(Otomobil, self).__init__(uretimYili,uretimYeri,marka,vitesTuru,renk,durum)

class Motosiklet(Arac):
    def __init__(self,motorh,yakit,emisyon,klima,ortyakit,lastikcap,model,lastiksayi,hiz,ekstra,uretimYili,uretimYeri,marka,vitesTuru,renk,durum):
        self.motorHacmi = motorh
        self.yakitTuru = yakit
        self.emisyon = emisyon
        self.klima = klima
        self.ortYakit = ortyakit
        self.lastikSayi = lastiksayi
        self.lastikCapi = lastikcap
        self.model = model
        self.hiz = hiz
        self.ekstraOzellik = ekstra
        super(Motosiklet, self).__init__(uretimYili,uretimYeri,marka,vitesTuru,renk,durum)
    def motorEkle(self,motor):
        motosikletler.append(motor)


class Kamyon(Arac):
    def __init__(self,damper,model,yakit,klima,lastikcap,dingil,hiz,ekstra,uretimYili,uretimYeri,marka,vitesTuru,renk,durum):
        self.damperSayi = damper
        self.yakitTuru = yakit
        self.klima = klima
        self.lastikCapi = lastikcap
        self.dingilSayi = dingil
        self.hiz = hiz
        self.model = model
        self.ekstraOzellik = ekstra
        super(Otomobil, self).__init__(uretimYili,uretimYeri,marka,vitesTuru,renk,durum)

class Bisiklet(Arac):
    def __init__(self,jantturu,sayi,kadro,jantboyut,frentip,tip,cinsiyet,susp,ekstra,uretimYili,uretimYeri,marka,vitesTuru,renk,durum):
        self.jantTuru = jantturu
        self.vitesSayisi = sayi
        self.kadroBoyu = kadro
        self.jantBoyutu = jantboyut
        self.frenTipi = frentip
        self.tip = tip
        self.cinsiyet = cinsiyet
        self.suspansiyon = susp
        self.ekstraOzellik = ekstra
        super(Otomobil, self).__init__(uretimYili,uretimYeri,marka,vitesTuru,renk,durum)

def motorListele():
    for i in motosikletler:
        print(i.motorHacmi,i.yakitTuru,i.emisyon,i.klima,i.ortYakit,i.lastikSayi,i.lastikCapi,i.model,i.hiz,i.ekstraOzellik)

a= Motosiklet("2.200","lpg","yok","yok","3","5","güzel","2","çok hızlı","içinde sigara içilmedi","1998","çin","batuha","vites yok","pembe","sıfır ayarında temiz kullanılmış 2. el")
a.motorEkle(a)
print(motosikletler)
motorListele()