valor1Str=input("Ingrese un numero: ")
try:
    valor1=int(valor1Str)   #valueError
    valor2=valor1+5
    print(f"Resultado {valor2}")
except:
    print("entro aqui al except")

print("FIN")