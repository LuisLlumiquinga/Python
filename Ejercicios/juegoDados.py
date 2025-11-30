import random

print("**** PRUEBA TU SUERTE ****")
print("Si obtienes un valor mayor a 8, ganas")

input("Presiona ENTER para lanzar el dado")

valorObtenido1=random.randint(1,6)
valorObtenido2=random.randint(1,6)

total=int(valorObtenido1)+int(valorObtenido2)

print(f"Ha obtenido {valorObtenido1} y {valorObtenido2}, total {total}")

if total<8:
    print("Lo siento no es tu dia de suerte, no te salvas")