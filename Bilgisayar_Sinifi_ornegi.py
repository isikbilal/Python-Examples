class Bilgisayar():

#2 = Bilgisayar() # __init__ metodu. İlk çalıştırıldığında çalışır

#print(pc) ##__str__ metodu. print fonksiyonu kullanıldığında çağırılır.

#del(pc) #__del__ fonksiyonu. Silmek için kullanılır.

    def __init__(self, pc_markasi, pc_modeli, pc_fiyati): #Method parametrelerini yazarken özel method da sadece ilk parametreyi self olarak yazıyoruz, diğerlerinin başına self. koymuyoruz, aşağıdaki gibi fonksiyonun içinde değerleri atarken self.pc_marka şeklinde kullanıyoruz.
        print ("İnit fonksiyonu... Nesne oluşturuldu.")
        self.pc_markasi = pc_markasi #Burada atama yaparken eşitliğin her iki tarfında da aynı kelime olmalı, yoksa hata veriyor. Örneğin self.pc_markasi = marka yazarsak hata veriyor. Fonksiyonun aldığı parametrenin isimini vermeliyiz yani. 
        self.pc_fiyati = pc_fiyati
        self.pc_modeli = pc_modeli

    def __str__(self):#self parametresini girmeyi unutma özel method tanımlarken.
        print("Bizim oluşturduğumuz print (__str__) fonksiyonu..")
        return "Pc Bilgileri:\nPc markası: {}\nPc Fiyatı: {}" .format(self.pc_markasi, self.pc_fiyati) #return'ü unutma, tırnakları kapattıktan sonra .format kullanabilirsin, 

    def __len__(self):
        print ("Len fonksiyonunda pc fiyatını döndürdük örnek olarak:")
        return len(self.pc_fiyati)

    def __del__(self):
        print("Obje siliniyor...")    

#Fonksiyonlarımızı bitirdik. Bu fonksiyonları tanımlarken class'ın içerisinde bir tab boşluk bıraktıktan sonra tanımlamaya dikkat et.
#class dan nesne (pc, pc1, pc2 vs.) türetirken de en dışta türet ki global olsun. 

pc = Bilgisayar("Monster", "Abra", "400")

print(pc)

print(pc.pc_fiyati) #Fiyatı bu şekilde aldık.

print(len(pc)) #Eğer fiyatı integer tipinde verirsek o şekilde çalışmıyor, string olarak verdiğimiz zaman da o string de kaç karakter varsa onun sayısını uzunluk olarak veriyor.

del(pc)

pc2 = Bilgisayar("Hp", "Elitebook", "5000")

print(pc2)

print(pc2.pc_fiyati)

print(len(pc2))
