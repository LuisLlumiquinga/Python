from random import randint

#Crear una funcion que retorne una lista
#con 5 numeros aleatorios
#entre 10 y 20, ambos incluidos

def generarAleatorio():
    lista=[]

    for num in range(5): #[0,1,2,3,4]
        lista.append(randint(10,20))
    
    return lista