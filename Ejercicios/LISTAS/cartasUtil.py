def calcularProbabilidadGanar(listaCartas, cartaMenor, cartaMayor):
    cartasGanadoras=0
    menor=obtenerValorCarta(cartaMenor)
    mayor=obtenerValorCarta(cartaMayor)

    for carta in listaCartas:
        cartaValor=obtenerValorCarta(carta)        

        if cartaValor>menor and cartaValor<mayor:
            cartasGanadoras+=1

    probabilidad=(cartasGanadoras/len(listaCartas))*100

    return round(probabilidad,2)

def obtenerValorCarta(carta):
    cartas=carta.split("-")
    valorCarta=int(cartas[3])

    return valorCarta