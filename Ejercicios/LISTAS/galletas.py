#retorna un mensaje aleatorio
#import random
from random import randint

def generarFortuna():
    mensajes=["Hoy es tu dia de suerte",    #0
              "Conoceras el amor",          #1
              "Otra cosa"]                  #2
    
    aleatorio=randint(0,2)
    
    return mensajes[aleatorio]