import tkinter as tk

#######funciones
def saludar():
    #get devuelve lo que ingreso el usuario como String
    nombre=txtNombre.get()
    #Modifica el texto de la etiqueta llamada lblMensaje
    #config modifica la propiedad o propiedades que recibe como parametro
    lblMensaje.config(text=f"Hola mijin {nombre}")

#######

#######grafica
#crea la ventana
ventana=tk.Tk()

#cambia el titulo de la ventana
ventana.title("BIENVENIDA")

lblIngrese=tk.Label(text="Ingrese su nombre")
lblIngrese.pack()

#ancho por alto de la ventana
ventana.geometry("600x300")

#Crea una caja de texto
txtNombre=tk.Entry()
txtNombre.pack()

#Crea un boton
btnOK=tk.Button(text="OK", command=saludar)

#pack agrega el boton a la ventana
btnOK.pack()

#Crea una etiqueta
lblMensaje=tk.Label(text="")

#pack agrega la etiqueta a la ventana
lblMensaje.pack()

#muestra la ventana
ventana.mainloop()