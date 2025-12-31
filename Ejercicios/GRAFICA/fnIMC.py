#***********FUNCION calcularIMC*******
#Recibe dos parámetros
#   peso: float, el peso de la persona en kilos
#   estatura: float, la estatura de la persona en CENTIMETROS
#Calcula el imc
#Antes de aplicar la fórmula transforme los CENTIMETROS en METROS
#Retornar el imc redondeado a 4 decimales, 
#puede usar la función round. Ejemplo: return round(imc,4)
def calcularIMC(peso, estatura):
    estaturaMetros=estatura/100
    IMC=peso/(estaturaMetros*estaturaMetros)

    return round(IMC,4)

#***********FUNCION interpretarIMC*******
#Recibe un parámetro
#   imc: float, el valor del imc de la persona
#RETORNA un mensaje del estado de la persona en base al valor
#recibido con la tabla de ejercicios anteriores, por ejemplo
#Obesidad Grado 3, Peso Normal, etc
#IMPORTANTE: colocar bien los extremos de los rangos 
def interpretarIMC(imc):
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