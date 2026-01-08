def calcularIVA(precio):
    calculo=precio*.15
    return round(calculo,2)

def calcularAporteEmpleado(sueldo):
    aporte=sueldo*0.0945
    return round(aporte,2)

def calcularAporteEmpresa(sueldo):
    aporte=sueldo*0.121
    return round(aporte,2)

def calcularDescuento(precioProducto, porcentajeDescuento):
    descuento=precioProducto*porcentajeDescuento/100
    return round(descuento,2)

def calcularPrecioFinal(precioProducto, porcentajeDescuento):
    descuento=calcularDescuento(precioProducto, porcentajeDescuento)
    precio=precioProducto-descuento
    return round(precio,2)