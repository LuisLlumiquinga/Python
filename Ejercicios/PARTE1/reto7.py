nombreUsuario=input("Ingrese su nombre: ")
edadUsuario=input("Ingrese su edad: ")
nombreAmigo=input("Ingrese el nombre de un amigo: ")
edadAmigo=input("Ingrese la edad de su amigo: ")

resultadoSuma=int(edadUsuario)+int(edadAmigo)
diferenciaEdades=int(edadUsuario)-int(edadAmigo)

print(f"La suma de las edades de {nombreUsuario} y {nombreAmigo} es {resultadoSuma}")

print(f"La diferencia de edades entre {nombreUsuario} y {nombreAmigo} es {diferenciaEdades}")