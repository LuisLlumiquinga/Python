estaturaStr=input("Ingrese su estatura: ")
estatura=float(estaturaStr)

edadStr=input("Ingrese su edad (1-100): ")
edad=int(edadStr)

if edad>=1 and edad<=100:
    print("Edad correcta")
    if edad<5 and estatura<1.2:
        print("Puedes usar el juego")
    else:
        print("Lo siento, este juego no es para ti")
else:
    print("Edad incorrecta")

