def calcularTotal(numeros):
    total=0
    tamanio=len(numeros)

    for indice in range(tamanio):
        num=numeros[indice]
        total+=num
    return total

def validarListas(listaOrigen, listaDestino):
    origen=calcularTotal(listaOrigen)
    destino=calcularTotal(listaDestino)

    if origen==destino:
        return True
    else:
        return False

def resolverProblema(listaOrigen, listaDestino):
    movimientos=[]

    cantidadMovimiento=0

    tamanioOrigen=len(listaOrigen)
    tamanioDestino=len(listaDestino)

    for indiceDestino in range(tamanioDestino):
        

        for indiceOrigen in range(tamanioOrigen):
            valorDestino=listaDestino[indiceDestino]
            valorOrigen=listaOrigen[indiceOrigen]
            #print(f"destino: {valorDestino} - origen: {valorOrigen}")

            if valorOrigen<valorDestino:
                cantidadMovimiento=valorOrigen
            else:
                cantidadMovimiento=valorDestino
            
           # print(f"{indiceOrigen} - {indiceDestino} - {cantidadMovimiento}")
            if cantidadMovimiento!=0:
                movimientos.append(f"{indiceOrigen}-{indiceDestino}-{cantidadMovimiento}")

            listaOrigen[indiceOrigen]-=cantidadMovimiento
            listaDestino[indiceDestino]-=cantidadMovimiento

            if listaDestino[indiceDestino]==0:
                
                break
    return movimientos

def recuperarCurso(infoEstudiante):
    partes=infoEstudiante.split("-")

    curso=int(partes[0])

    return curso

def retornarNombreCompleto(infoEstudiante):
    partes=infoEstudiante.split("-")
    nombre=partes[1]
    apellido=partes[2]

    nombreCompleto=(f"{nombre} {apellido}")
    return nombreCompleto

def recuperarNota(infoEstudiante):
    partes=infoEstudiante.split("-")
    nota=int(partes[3])
    return nota

def buscarEstudiante(listaEstudiantes, numeroCurso, nota):
    for estudiante in listaEstudiantes:  
        curso=recuperarCurso(estudiante)
        notaEncontrada=recuperarNota(estudiante)        

        if curso==numeroCurso and notaEncontrada==nota:
            nombre=retornarNombreCompleto(estudiante)
            return nombre
    return None

lista=["1-juan-perez-10", "2-rosario-tijeras-10", "3-alam-brito-9"]

for elemento in lista:
    partes=elemento.split("-")
    if int(partes[0])==1 and int(partes[3])==10:
        print(partes[1])

    
    