def buscarEstudiante(cedula, listaEstudiante):
    for est in listaEstudiante:
        partesEstudiante=est.split("#")
        if partesEstudiante[0]==cedula:
            return est
    return None

def calcularTotal(n1, n2, n3, faltas):
    if faltas==0:
        n4=10
    elif faltas>=1 and faltas<4:
        n4=9
    elif faltas==4 or faltas==5:
        n4=8
    elif faltas>5:
        n4=7
    
    promedio=(n1+n2+n3+n4)/4

    return round(promedio, 2)