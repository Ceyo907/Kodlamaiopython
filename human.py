class Human:
    #name = "Ceyhun" #--> default value
    #built-in
    #initiliaze
    def __init__(self,name):#--> Constructor (yapıcı) blok
        self.name = name # Değişken tanımlama
        print("Bir human instance'i üretildi.")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer : {self.name}"
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")