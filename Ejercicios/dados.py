import random

print("**** PRUEBA TU SUERTE ****")
print("Si obtienes un valor mayor a 3, ganas")

input("Presiona ENTER para lanzar el dado")

valorObtenido=random.randint(1,6)

print(f"Obtuviste un {valorObtenido}")

if valorObtenido==6:
    print("Felicidades Ganaste!!")
    print("Estas de suerte")