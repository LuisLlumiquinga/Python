from tkinter import Tk, Entry, Label, Button
from galletas import generarFortuna

#FUNCIONES
def fnGenerar():
    mensaje=generarFortuna()
    lblMensaje.config(text=mensaje)

#PARTE GRAFICA
ventana=Tk()
ventana.geometry("200x200")
ventana.title("Galletas Fortuna")

lblFortuna=Label(text="Prueba tu fortuna")
lblFortuna.pack()

btnPresionar=Button(text="PRESIONAME", command=fnGenerar)
btnPresionar.pack()

lblMensaje=Label(text="", fg="red")
lblMensaje.pack()

ventana.mainloop()