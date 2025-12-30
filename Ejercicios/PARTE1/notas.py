notaExamen=int(input("Ingrese su nota del examen (1-10): "))

if notaExamen<=10 and notaExamen>=0:
    print("Es una nota valida")
    
    inasistencias=int(input("Ingrese las veces a faltado a clases: "))

    if inasistencias<3 and notaExamen>=8:
        print("APROBADO")
    else:
        print("REPROBADO")
else:
    print("Solo se permiten notras entre 1 y 10")

print("FIN DEL PROGRAMA")