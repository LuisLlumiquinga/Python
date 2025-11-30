import random

numeroUsuario=int(input("Adivina un numero del 1 al 5: "))
numeroAleatorio=random.randint(1,6)

print(f"El numero correcto era el {numeroAleatorio}")

if numeroUsuario==numeroAleatorio:
    print("Felicidades Ganaste!!")
    print("Estas de suerte")

