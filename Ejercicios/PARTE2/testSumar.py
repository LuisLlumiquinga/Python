import funciones

valor1Str=input("Ingrese valor 1: ")
valor2Str=input("Ingrese valor 2: ")

v1=int(valor1Str)
v2=int(valor2Str)

resultado=funciones.sumar(v1, v2)

print(f"La suma de {v1} + {v2} es {resultado}")