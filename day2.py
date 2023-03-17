faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi))
faiz = str(faiz)
print(type(faiz))

vade=int(input("Lütfen istediğiniz vade sayısını giriniz : "))
print(type(vade))
vade= vade + 12

# string interpolation
# seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
