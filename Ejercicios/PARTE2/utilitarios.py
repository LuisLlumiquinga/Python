def calcularPromedio(nota1, nota2, nota3):
    promedio=(nota1+nota2+nota3)/3
    return promedio

def consultarMulta(tipoMulta):
    if tipoMulta==1:
        multa=10
    elif tipoMulta==2:
        multa=15
    elif tipoMulta==3:
        multa=20
    elif tipoMulta==4:
        multa=30
    else:
        multa=-1
    return multa

def calcularValorHora(salario):
    valorHora=salario/160
    return valorHora

def calcularSubtotal(precioProducto, cantidad, porcentajeDescuento):
    subtotalSinDescuento=precioProducto*cantidad

    descuento=subtotalSinDescuento*porcentajeDescuento/100

    subtotal=subtotalSinDescuento-descuento

    return subtotal

def calcularValorDescuento(precio, porcentajeDescuento):
    descuento=precio*porcentajeDescuento/100
    return descuento