#import tkinter as tk #importar el modulo completo
from tkinter import Tk, Label, Entry, Button
contactos=[]

#FUNCIONES
def fnGuardar():
    nombre=txtNombre.get()  #obtener el nombre ingresado
    contactos.append(nombre)    #agrega el nombre a la lista
    print(contactos)

#PARTE GRAFICA
ventana=Tk()
ventana.geometry("300x300")
ventana.title("CONTACTOS")
lblNombre=Label(text="Ingrese su nombre: ")
lblNombre.pack()

txtNombre=Entry()
txtNombre.pack()

btnGuardar=Button(text="GUARDAR", command=fnGuardar)
btnGuardar.pack()

ventana.mainloop()

