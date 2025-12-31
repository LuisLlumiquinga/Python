def determinarResultadosIMC(imc):
    if imc>=0 and imc<16:
        mensaje="Delgadez severa"
    elif imc>=16 and imc<17:
        mensaje="Delgadez moderada"
    elif imc>=17 and imc<18.5:
        mensaje="Delgadez leve"
    elif imc>=18.5 and imc<25:
        mensaje="Peso normal"
    elif imc>=25 and imc<30:
        mensaje="Sobrepeso"
    elif imc>=30 and imc<35:
        mensaje="Obesidad Grado 1"
    elif imc>=35 and imc<40:
        mensaje="Obesidad Grado 2"
    elif imc>=40:
        mensaje="Obesidad Grado 3"
    else:
        mensaje="IMC fuera de rango"
    
    return mensaje

def encontrarMayor(valor1, valor2, valor3):
    mayorActual=valor1

    if valor2>mayorActual:
        mayorActual=valor2
    
    if valor3>mayorActual:
        mayorActual=valor3
    
    return mayorActual

def encontrarMenor(valor1, valor2, valor3, valor4):
    menorActual=valor1

    if valor2<menorActual:
        menorActual=valor2
    
    if valor3<menorActual:
        menorActual=valor3
    
    if valor4<menorActual:
        menorActual=valor4

    return menorActual

def calcularEdad(anioNacimiento):
    anioActual=2025

    if anioNacimiento>=0 and anioNacimiento<=anioActual:
        edad=anioActual-anioNacimiento
        return edad
    
    else:
        return -1
    
def calcularCuota(monto, interesAnual, numeroMeses):
    i=(interesAnual/12)/100

    cuotaMensual=(monto*i)/(1-(1+i)**(-numeroMeses))

    return cuotaMensual