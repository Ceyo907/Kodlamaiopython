faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi))
faiz = str(faiz)
#print(type(faiz))

vade=36 #int(input("Lütfen istediğiniz vade sayısını giriniz : "))
print(type(vade))
vade= vade + 12

# string interpolation
# seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "Ceyhun" #input("isminizi giriniz: ")
metin="Merhaba {name}".format(name=123)
print(metin)

#f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)

#listeler
#döngüler
#fonksiyonlar

dizi = ["İhtiyaç Kredisi",10,5.2,True]
print(dizi)

krediler=["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))
print(krediler[0])

print(len(krediler))  #length
#print(krediler[3])--> hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)
krediler.pop(0)
print(krediler)
krediler.append("Taşıt Kredisi")
print(krediler)
krediler.remove("Taşıt Kredisi")
print(krediler)
krediler.extend(["Y Kredisi","Z kredisi"])
print(krediler)

#for
#i=0 i<10

for i in range(10):
    print("xx")
    print(i)
print("***************")
for i in range (5,11):
    print(i)
print("***************")
for i in range (0,51,10):
    print(i)
print("*************")
# for i in range(0.1,0.5):
#     print(i)

krediler=["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]

for kredi in krediler:
    print(kredi)
print("******************")

for i in range(len(krediler)):
    print(krediler[i])
print("**************")

#sonsuz döngü
i = 0
while i<10:
    print("x")
    i+=1
print("y")
print("*******************")

while True:
    print("X")
    break
print("*******************")
i = 0
while i<len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i]== "Konut Kredisi":
        break
    

# fonksiyonlar

fiyat = 100
indirim = 20

#definition
def calculate():
    print(100-20)
    
def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)
    
def sayHello(name):
    print(f"Merhaba {name}")
    
calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Ceyhun")
sayHello("Amet")

def calculateAndReturn(price,discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)


# sınıflar => claslar
# modules
# paket yönetimi
