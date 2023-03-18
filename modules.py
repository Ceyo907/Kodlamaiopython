#alias--> isimlendirme,takma isim
#import matematik as m
from matematik import topla as toplamaIslemi
from day2 import sayHello
from human import Human
# built-in modules
import random
from seleniumExample import webdriver
#package
print(toplamaIslemi(10,20))

print(random.randint(0,100))#--> 0-100 arasında rastgele sayı üretir.

human1=Human("Mirza")
human1.talk("Merhaba")

chromeDriver = webdriver.Chrome()
#packages 