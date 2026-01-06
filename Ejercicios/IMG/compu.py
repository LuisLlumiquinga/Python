from tkinter import *
from utilitariosImagen import obtenerImagen

def encender():
    img1=obtenerImagen("compuPrendida.png", 200)
    lblImagen.config(image=img1)
    lblImagen.image=img1

    btnEncender.config(state="disabled")
    btnApagar.config(state="normal")

def apagar():
    img1=obtenerImagen("compuApagada.png", 200)
    lblImagen.config(image=img1)
    lblImagen.image=img1

    btnEncender.config(state="normal")
    btnApagar.config(state="disabled")

ventana=Tk()
ventana.geometry("500x500")
ventana.title("Imagenes")

img1=obtenerImagen("compuApagada.png", 200)
lblImagen=Label(image=img1)
lblImagen.pack()

btnApagar=Button(text="APAGAR", command=apagar, state="disabled")
btnApagar.pack()

btnEncender=Button(text="ENCENDER", command=encender)
btnEncender.pack()

ventana.mainloop()