class Hayvan():
    def __init__(self, türü, göz_şekli, göz_rengi, ayak_sayısı, hareket_hızı):

        print("Hayvan sınıfının init fonksiyonu...")

        self.türü = türü
        self.göz_şekli = göz_şekli
        self.göz_rengi = göz_rengi
        self.ayak_sayısı = ayak_sayısı
        self.hareket_hızı = hareket_hızı

    def bilgilerigöster(self):

        print("Hayvan sınıfının bilgileri...")

        print("""
        Hayvanın bilgileri:
        Tür: {}
        Göz şekli: {}
        Göz rengi: {}
        Ayak sayısı: {}
        Hareket_hızı: {}
        """.format(self.türü,self.göz_şekli,self.göz_rengi, self.ayak_sayısı, self.hareket_hızı))

    def solunumyap(self, solunum_türü):
        print("{} solunumu yapılıyor.".format(solunum_türü))

    def hareketet(self, hareket_şekli):
        print("{} şeklinde hareket ediyor".format(hareket_şekli))

    def hızlandır(self, hızlanma_miktarı):
        print("Hızlandırılıyor...")
        self.hareket_hızı = self.hareket_hızı + hızlanma_miktarı    
        print("Yeni hız: {}".format(self.hareket_hızı))
                


h1 = Hayvan("Hayvanın türü", "Hayvanın göz şekli", "Hayvanın göz rengi", 2, 10 )
print(h1)
h1.bilgilerigöster()
h1.solunumyap("Akciğer")
h1.hareketet("Yürümek")
h1.hızlandır(5)


class Kuş(Hayvan):
    def __init__(self, türü, göz_şekli, göz_rengi, ayak_sayısı, hareket_hızı, kanat_şekli): #Overriding (Overrride etmek). Burada kuş sınıfından oluşturulacak nesneler için başka bir __init__ fonksiyonu tanımlayarak daha öncesinde kalıtım yaptığımız Hayvan sınıfının __init__ fonksiyonunu override etmiş (ezmiş) oluyoruz.
        
        # self.türü = türü
        # self.göz_şekli = göz_şekli
        # self.göz_rengi = göz_rengi
        # self.ayak_sayısı = ayak_sayısı
        # self.hareket_hızı = hareket_hızı
        super().__init__(türü, göz_şekli, göz_rengi, ayak_sayısı, hareket_hızı) #Burada Hayvan sınıfından Override ettiğimiz __init__ fonksiyonunun içerisindeki "self.türü = türü", "self.göz_şekli = göz_şekli" vs. gibi özellikleri tekrardan yazmamak için super() methodunu kullandık.
        
        print("Kuş sınıfının init fonksiyonu...") #Artık Kuş sınıfıdnan bir nesne oluşturduğumuzda buradaki init fonksiyonu çalışcak ve aşağıdaki gibi kanat_şekli özelliği ile oluşacak.
        
        self.kanat_şekli = kanat_şekli #Yukarıdaki satırda super() methoduyla Hayvan sınıfının özelliklerini aldıktan sonra bu satırda da Hayvan sınıfında olmayıp Kuş sınıfımıza özgü bir özellik olan "kanat_şekli" özelliğini ekledik

    def bilgilerigöster(self):#Burada da yine __init__ fonksiyonunda olduğu gibi bilgilerigöster() fonksiyonunu da "kanat_şekli" değerini içerecek şekilde override ettik.
        print("Kuş sınıfının bilgileri...")

        print("""
        Kuşun bilgileri:
        Tür: {}
        Göz şekli: {}
        Göz rengi: {}
        Ayak sayısı: {}
        Hareket hızı: {}
        Kanat şekli: {}
        """.format(self.türü,self.göz_şekli,self.göz_rengi, self.ayak_sayısı, self.hareket_hızı, self.kanat_şekli))

    def öt(self): #Hayvan sınıfındaki methodlarla birlikte üstüne kendimiz de öt methodu gibi başka methodlar ekleyerek onları da kullanabiliriz.
        print("Cik cik cik...")

k1 = Kuş("Karga", "Yuvarlak gözlü", "Siyah", 2, 20, "Üçgen kanat") #Artık burada kuş sınıfının __init__ methodu çağrıldığı için parametre olarak kanat_şekli için de "Üçgen kanat" gibi bir değer vermemiz gerekiyor.
print(k1)

k1.bilgilerigöster()
k1.hareketet("Uçarak")
k1.hızlandır(15)
k1.bilgilerigöster()
print(dir(Kuş)) #Hayvan sınıfından türetilmiş Kuş sınıfının özellikleri. Dikkat ederseniz Hayvan sınıfı ile aynı bu özellikler
print(dir(k1)) #Kuş sınıfından türetilmiş k1 nesnesinin(objesinin) özellikleri.
k1.öt()

k2 = Kuş("Papağan", "Elips gözlü", "Yeşil", 2, 15, "Yaprak kanat")
k2.bilgilerigöster()

class Köpek(Hayvan):
    def __init__(self, türü, göz_şekli, kulak_şekli, göz_rengi, ayak_sayısı, hareket_hızı, kuduz_mu): #Yine override ettik Hayvan sınıfından

        super().__init__(türü,göz_şekli, göz_rengi, ayak_sayısı, hareket_hızı) #Yine super() ile önceki Hayvan sınıfının attribute(özellik)'lerini aldık tek tek yazmadan 

        print("Köpek sınıfının init fonksiyonu.")
        self.kulak_şekli = kulak_şekli
        self.kuduz_mu = kuduz_mu

    def bilgilerigöster(self):#Override örneği.
        
        super().bilgilerigöster() #super() örneği. Parametre almayan fonksiyonlarda da bu şekilde oluyor. Methoda parametre vermeden yapıyoruz yani.

        print("Köpek sınıfının bilgileri.")

        print("""
        Köpeğin bilgileri:
        Kulak şekli: {}
        Kuduz mu: {}
        """.format(self.kulak_şekli, self.kuduz_mu))

    def aşıla(self):
        if(self.kuduz_mu == True):
            self.kuduz_mu = False
            print("Köpek aşılandı.")
        else:
            print("Köpek zaten aşılı")        

        
kopek1 = Köpek("Kangal", "Oval gözlü", "Yaprak kulaklı", "Kahverengi gözlü", 4, 65, True)
print(kopek1)
kopek1.bilgilerigöster()
kopek1.aşıla() #Metodu ilk çalıştırmamızda köpek sunıfında türetilen nesneler default olarak kuduz_mu = True şeklinde geldiği için ilk çalıştırmamızda köpeği aşıladık ve kuduz durumunu False yaptık 
kopek1.bilgilerigöster()
kopek1.aşıla()#İkinci çalıştırmamızda ise "kuduz_mu" durumunu en son False yaptığımız için aşıla() fonksiyonundaki if else bloğuna takıldı ve aşılamayı yapamadı.


