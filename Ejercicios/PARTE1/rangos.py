calificacionStr=input("Ingrese su calificacion (0.0-10.0): ")
calificacion=float(calificacionStr)

if calificacion>=0 and calificacion<=4:      #[0-4]
    print("Debes mejorar")
elif calificacion>4 and calificacion<=6:    #]4-6]
    print("Muy bien")
elif calificacion>6 and calificacion<=10:  #]6-10]
    print("Excelente")
else:
    print("Nota incorrecta")