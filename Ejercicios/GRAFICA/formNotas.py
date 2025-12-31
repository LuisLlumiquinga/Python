import tkinter as tk
import fnNotas
#********FUNCIONES*******
def limpiar():
    lblErrorN1.config(text="")
    lblErrorN2.config(text="")
    lblErrorN3.config(text="")

def btnCalcularPromedio():
    limpiar()

    nota1Str=txtNota1.get()
    valorNota1=float(nota1Str)
    if valorNota1<0 or valorNota1>10:
        lblErrorN1.config(text="La nota debe ser un valor entre 0 y 10")

    nota2Str=txtNota2.get()
    valorNota2=float(nota2Str)

    if valorNota2<0 or valorNota2>10:
        lblErrorN2.config(text="La nota debe ser un valor entre 0 y 10")

    nota3Str=txtNota3.get()
    valorNota3=float(nota3Str)

    if valorNota3<0 or valorNota3>10:
        lblErrorN3.config(text="La nota debe ser un valor entre 0 y 10")

    if (valorNota1>=0 and valorNota1<=10) and (valorNota2>=0 and valorNota2<=10) and (valorNota3>=0 and valorNota3<=10):
        promedio=fnNotas.calcularPromedio(valorNota1,valorNota2,valorNota3)
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