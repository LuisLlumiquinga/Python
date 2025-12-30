import random
import funciones

nombre1=input("Ingrese nombre del primer jugador: ")
nombre2=input("Ingrese nombre del segundo jugador: ")
print("Para lanzar los dado presione ENTER")
input(f"Lanza {nombre1}")
dado1Jugador1=random.randint(1,6)
dado2Jugador1=random.randint(1,6)
total1=dado1Jugador1+dado2Jugador1

funciones.mostrarLanzamiento(nombre1, dado1Jugador1, dado2Jugador1)

input(f"Lanza {nombre2}")
dado1Jugador2=random.randint(1,6)
dado2Jugador2=random.randint(1,6)
total2=dado1Jugador2+dado2Jugador2

funciones.mostrarLanzamiento(nombre2, dado1Jugador2, dado2Jugador2)

if total1>total2:
    funciones.mostrarGanador(nombre1)
elif total2>total1:
    funciones.mostrarGanador(nombre2)
else:
    print("ES UN EMPATE!!")