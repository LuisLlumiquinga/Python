def calcularInteresSimple(monto, plazo, tasa):
    interesSimple=(monto*tasa/100)*plazo

    return interesSimple

def calcularInteresCompuesto(monto, plazo, tasa):
    capitalFinal=monto*(1+tasa/100)**plazo

    interesCompuesto=capitalFinal-monto

    return round(interesCompuesto, 2)

def calcularCuota(montoPrestamo, tasa, plazo):
    pago=montoPrestamo*(((1+tasa/100)**plazo)*(tasa/100))/(((1+tasa/100)**plazo)-1)

    return round(pago, 2)
