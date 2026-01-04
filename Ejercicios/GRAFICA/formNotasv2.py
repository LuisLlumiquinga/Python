import tkinter as tk
import fnNotas

existeErrores=False #variable global

#********FUNCIONES*******
def validarNota(valorNota, labelError):
    #Fuera del rango
    if valorNota<0 or valorNota>10:
        labelError.config(text="La nota debe ser un valor entre 0 y 10")
        global existeErrores    #avisar que se va a cambiar el valor de la variable global
        existeErrores=True

def limpiar():
    lblErrorN1.config(text="")
    lblErrorN2.config(text="")
    lblErrorN3.config(text="")
    lblPromedio.config(text="Promedio:0")
    global existeErrores
    existeErrores=False

#obtiene el flotante de una caja de texto
def obtenerFloat(cajaTexto, lblError):
    valorStr=cajaTexto.get()
    try:
        valorNota=float(valorStr)
        validarNota(valorNota, lblError)
    except:
        lblError.config(text="Debe ingresar un numero")
        global existeErrores
        existeErrores=True
        valorNota=None
    return valorNota

def btnCalcularPromedio():
    limpiar()

    valorNota1=obtenerFloat(txtNota1, lblErrorN1)
    valorNota2=obtenerFloat(txtNota2, lblErrorN2)
    valorNota3=obtenerFloat(txtNota3, lblErrorN3)

    if existeErrores==False:
        promedio=fnNotas.calcularPromedio(valorNota1, valorNota2, valorNota3)
        lblPromedio.config(text=f"Promedio:{promedio}")

#********GRAFICA*********
ventana=tk.Tk()
ventana.title("PROMEDIO")
ventana.geometry("400x400")

lblNota1=tk.Label(text="Nota 1")
lblNota1.pack()
txtNota1=tk.Entry()
txtNota1.pack()
lblErrorN1=tk.Label(text="", fg="red")
lblErrorN1.pack()

lblNota2=tk.Label(text="Nota2")
lblNota2.pack()
txtNota2=tk.Entry()
txtNota2.pack()
lblErrorN2=tk.Label(text="", fg="red")
lblErrorN2.pack()

lblNota3=tk.Label(text="Nota3")
lblNota3.pack()
txtNota3=tk.Entry()
txtNota3.pack()
lblErrorN3=tk.Label(text="", fg="red")
lblErrorN3.pack()

btnPromedio=tk.Button(text="PROMEDIO",command=btnCalcularPromedio)
btnPromedio.pack()
lblPromedio=tk.Label(text="Promedio:0")
lblPromedio.pack()
ventana.mainloop()