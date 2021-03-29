import random #Rastgele kanal değiştirmek için kullanacağız.
import time # Kanal eklerken sleep ile 1 sn bekletmek için kullancağız

class Kumanda():
    #init fonk. obje oluşturulurken çağrılan ilk fonksiyon, yani constructor. 
    # Burada init fonksiyonunu kendimiz modifiye ederek Kumanda sınıfından türeteceğimiz objelerin hangi özellikler ile oluşturulacağını belirliyoruz.
    def __init__(self, tv_durum="Kapalı", ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        self.tv_durum=tv_durum
        self.ses=ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
        #Constructor fonksiyonumuz bitti, artık Kumanda sınıfından bir kumanda objesi türettiğimizde bu default özelliklerle oluşturulacak.   

    def tv_ac(self):
        if(self.tv_durum == "Kapalı"):
            self.tv_durum = "Açık"
            print("Tv açıldı...")
        else:
            print("Tv zaten açık")

    def tv_kapat(self):
        if(self.tv_durum == "Açık"):
            self.tv_durum = "Kapalı"
            print("Tv kapandı...")
        else:
            print("Tv zaten kapalı")

    def ses_ayari(self):
        while True:
            cevap = input("Sesi azaltmak için '<', arttırmak için '>' tuşuna basın. Çıkış için 'q' tuşuna basın...")
            if(cevap == "<"):
                if(self.ses > 0):
                    self.ses = self.ses-1
                    print("Ses:", self.ses)
                else:
                    print("Ses zaten en az seviyede...")
                
            elif(cevap == ">"):# Burada else durumunda birşey yapmamıza gerek olmadığı için aşağıda direk elif durumuna geçiyoruz.
                if(self.ses < 32): # Eski tv'lerde ses 32 den yukarı arttırılamadığı için max ses sınırını 32 yaptık.    
                    self.ses = self.ses+1
                    print("Ses:", self.ses)
                else:
                    print("Ses zaten maximum seviyede...")

            elif(cevap == "q"):
                print("Ses güncellendi: ",self.ses)
                print("Çıkış yapılıyor...")
                break
            
            else:
                print("Geçersiz bir tuş girdiniz. Lütfen tekrar deneyin.") 

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor..")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")

    def kanal_listele(self):
        print("Kanalların listesi: ", self.kanal_listesi)

    def rastgele_kanal_degistir(self):
        print("Kanal değiştiriliyor...")
        rastgele_kanal = random.randint(0,len(self.kanal_listesi)-1)
        print("Rastgele alınan kanalın indexi: ", rastgele_kanal)
        self.kanal = self.kanal_listesi[rastgele_kanal]  
        print("Kanal: ", self.kanal)

    def __len__(self): #Kanal sayısını almak istediğimizde buradaki len fonksiyonunu kullanmak için modifiye ediyoruz kanalların sayısını verecek şekilde
        return len(self.kanal_listesi) #Özel method ( __ ile başlayan methodlar ) tanımlarken return kullanırız


    def __str__(self): #Tv durumu için de aynı şekilde print fonksiyonunun kullandığı str yi modifiye ettik
        return "Tv Durumu : {}\nSes: {}\nKanallar: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.ses,self.kanal_listesi,self.kanal)

    def mute(self):
        self.ses = 0
        print ("Ses kapatıldı")
        print("Ses: ", self.ses)

kumanda = Kumanda()

print("""*******************

Televizyon Uygulaması

İşlemler ;

1. Televizyonu Aç

2. Televizyonu Kapat

3. Televizyon Bilgileri

4. Kanal Sayısını Öğrenme

5. Kanal Ekle

6. Rastgele Kanal'a Geç

7. Sesi Azalt Ya da Artır

8. Sesi kapat

Çıkmak için 'q' ya basın.

*******************""")

while True:

    islem = input("Lütfen bir işlem seçiniz: ")

    if(islem == "1"):
        kumanda.tv_ac()
    elif(islem == "2"):
        kumanda.tv_kapat()

    elif(islem == "3"):
        #kumanda.__str__() Bu şekilde yazamayız. print fonksiyonu ilk çağrıldığında __str__ fonksiyonunu çağırıyor ama biz kullanırken yine print olarak kullanmak zorundayız.       
        print(kumanda)

    elif (islem == "4"): # Her ikisi de oluyor.
        print("Lenght: ",len(kumanda)) 
        print("Kanal sayısı:",len(kumanda.kanal_listesi))
        

    elif(islem == "5"):
        eklenecek_kanal_listesi = input("Lütfen ekleyeceğiniz kanalları aralarına ',' koyarak giriniz: ")
        eklenecek_kanallar = eklenecek_kanal_listesi.split(",")
        for i in eklenecek_kanallar:
            kumanda.kanal_ekle(i)

    elif(islem == "6" ):
        kumanda.rastgele_kanal_degistir()

    elif(islem == "7"):
        kumanda.ses_ayari()

    elif(islem == "8"):
        kumanda.mute()    

    elif(islem == "q"):
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz bir işlem girdiniz. Lütfen tekrar ddeneyiniz.")    

            
