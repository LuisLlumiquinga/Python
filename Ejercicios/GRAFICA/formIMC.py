import tkinter as tk
import fnIMC

#*********FUNCIONES********
def btnCalcularIMC():
    limpiar()

    peso=float(txtPeso.get())
    estatura=float(txtEstatura.get())

    mensajePeso=validarRangos(peso, lblErrorPeso, 0, 150)
    mensajeEstatura=validarRangos(estatura, lblErrorEstatura, 30, 230)
    
    if mensajePeso==1 and mensajeEstatura==1:
        IMC=fnIMC.calcularIMC(peso, estatura)
        lblIMC.config(text=f"Su IMC es: {IMC}")

        interprete=fnIMC.interpretarIMC(IMC)
        lblInterpretacion.config(text=f"RESULTADO: {interprete}")

def validarRangos(valor, lblError, desde, hasta):
    if valor>hasta or valor<desde:
        lblError.config(text=f"Ingrese un valor entre {desde} y {hasta}")
    else:
        return 1

def limpiar():
    lblErrorEstatura.config(text="")
    lblErrorPeso.config(text="")
    lblIMC.config(text="Su IMC es:")
    lblInterpretacion.config(text="")

#*********PARTE VISUAL*****
ventana=tk.Tk()
ventana.geometry("400x400")
ventana.title("INDICE DE MASA CORPORAL")
lblIngresePeso=tk.Label(text="Ingrese su peso en kilos")
lblIngresePeso.pack()
txtPeso=tk.Entry()
txtPeso.pack()
lblErrorPeso=tk.Label(text="",fg="red")
lblErrorPeso.pack()

lblIngreseEstatura=tk.Label(text="Ingrese su estatura en centimetros")
lblIngreseEstatura.pack()
txtEstatura=tk.Entry()
txtEstatura.pack()
lblErrorEstatura=tk.Label(text="",fg="red")
lblErrorEstatura.pack()

btnIMC=tk.Button(text="CALCULAR IMC", command=btnCalcularIMC)
btnIMC.pack()

lblIMC=tk.Label(text="Su IMC es:",fg="blue")
lblIMC.pack()
lblInterpretacion=tk.Label(text="",fg="blue")
lblInterpretacion.pack()
ventana.mainloop()
