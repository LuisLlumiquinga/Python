import random

print("**** PRUEBA TU SUERTE ****")
input("Presiona ENTER para lanzar el dado")

total=random.randint(1,6)

print(f"Ha obtenido {total}")

if total==1:
    print("Lo siento no es tu dia de suerte, intenta nuevamente")
elif total==2:
    print("Lo siento no es tu dia de suerte, haz 5 flexiones")
elif total==3:
    print("Lo siento no es tu dia de suerte, corre por 30 segundos")
elif total==4:
    print("Lo siento no es tu dia de suerte, haz 5 burpies")
elif total==5:
    print("Lo siento no es tu dia de suerte, descansa 10 minutos")
elif total==6:
    print("Lo siento no es tu dia de suerte, vuelve manana")

print("Gracias, buen dia")