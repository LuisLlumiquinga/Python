from tkinter import *
from utilitariosImagen import obtenerImagen

ventana=Tk()
ventana.geometry("500x500")
ventana.title("Imagenes")

img1=obtenerImagen("emoji1.jpg", 200)
lblImagen1=Label(image=img1)
lblImagen1.pack()

ventana.mainloop()