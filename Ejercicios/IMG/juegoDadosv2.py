from tkinter import *
from utilitariosImagen import obtenerImagen
from random import randint

valorJugador1=0
valorJugador2=0
puntajeJugador1=0
puntajeJugador2=0

def fnNuevaPartida():
    global valorJugador2
    global valorJugador1
    global puntajeJugador1
    global puntajeJugador2
    
    lblDadoJugador1.config(image=imagenes[0])
    lblDadoJugador2.config(image=imagenes[0])
    lblResultado.config(text="")
    
    valorJugador1=0
    valorJugador2=0
    btnLanzar1.config(state="normal")
    btnLanzar2.config(state="normal")
    btnNuevaPartida.config(state="disabled")

    if puntajeJugador1==3 or puntajeJugador2==3:
        puntajeJugador1=0
        puntajeJugador2=0
        lblPuntajeJugador1.config(text=puntajeJugador1)
        lblPuntajeJugador2.config(text=puntajeJugador2)


def fnLanzarDadoJugador1():
    global valorJugador1
    valorJugador1=randint(1,6)
    lblDadoJugador1.config(image=imagenes[valorJugador1])
    btnLanzar1.config(state="disabled")
    if valorJugador2 != 0:
        fnDeterminarGanador()
        btnNuevaPartida.config(state="normal")

def fnLanzarDadoJugador2():
    global valorJugador2
    valorJugador2=randint(1,6)
    lblDadoJugador2.config(image=imagenes[valorJugador2])
    btnLanzar2.config(state="disabled")
    if valorJugador1 !=0:
        fnDeterminarGanador()
        btnNuevaPartida.config(state="normal")

def fnDeterminarGanador():
    btnNuevaPartida.config(state="normal")
    if valorJugador1>valorJugador2:
        lblResultado.config(text="Gana el Jugador 1")
        global puntajeJugador1
        puntajeJugador1+=1
        lblPuntajeJugador1.config(text=puntajeJugador1)

    elif valorJugador2>valorJugador1:
        lblResultado.config(text="Gana el Jugador 2")
        global puntajeJugador2
        puntajeJugador2+=1
        lblPuntajeJugador2.config(text=puntajeJugador2)

    else:
        lblResultado.config(text="EMPATE")
    
    imgGanar=obtenerImagen("ganar.jpg", 100)
    imgPerder=obtenerImagen("perder.png", 100)

    if puntajeJugador1==3:
        lblDadoJugador1.config(image=imgGanar)
        lblDadoJugador1.image=imgGanar
        
        lblDadoJugador2.config(image=imgPerder)
        lblDadoJugador2.image=imgPerder

    if puntajeJugador2==3:
        lblDadoJugador1.config(image=imgPerder)
        lblDadoJugador1.image=imgPerder
        
        lblDadoJugador2.config(image=imgGanar)
        lblDadoJugador2.image=imgGanar        

ventana=Tk()
ventana.geometry("500x400")
ventana.title("JUEGO DADOS")

imagenes=[
    obtenerImagen("dadoIncognita.png",100),#0
    obtenerImagen("dados1.png",100),#1
    obtenerImagen("dados2.png",100),#2
    obtenerImagen("dados3.png",100),
    obtenerImagen("dados4.png",100),
    obtenerImagen("dados5.png",100),
    obtenerImagen("dados6.png",100)#6
]

framePrincipal=Frame(ventana,bg="white")
framePrincipal.place(x=50,y=50)

lblTitulo=Label(framePrincipal,text="VEAMOS QUIEN ES EL MEJOR",font=("Arial", 15),bg="white")
lblDadoJugador1=Label(framePrincipal,image=imagenes[0])
btnLanzar1=Button(framePrincipal,text="LANZAR",command=fnLanzarDadoJugador1,bg="black",fg="white",font=("Arial", 12))
lblDadoJugador2=Label(framePrincipal,image=imagenes[0])
btnLanzar2=Button(framePrincipal,text="LANZAR",command=fnLanzarDadoJugador2,bg="black",fg="white",font=("Arial", 12))
lblResultado=Label(framePrincipal,text="",fg="red",font=("Arial", 15),bg="white")
btnNuevaPartida=Button(framePrincipal,text="NUEVA PARTIDA",command=fnNuevaPartida,bg="lime",font=("Arial", 12))
lblPuntajeJugador1=Label(framePrincipal,text="0",fg="blue",font=("Arial", 25),bg="white")
lblPuntajeJugador2=Label(framePrincipal,text="0",fg="blue",font=("Arial", 25),bg="white")

lblTitulo.grid(row=0,column=0,columnspan=3,padx=50)
lblResultado.grid(row=4,column=0,columnspan=3)
lblPuntajeJugador1.grid(row=1,column=0)
lblPuntajeJugador2.grid(row=1,column=2)
lblDadoJugador1.grid(row=2,column=0)
lblDadoJugador2.grid(row=2,column=2)
btnLanzar1.grid(row=3,column=0,pady=20)
btnLanzar2.grid(row=3,column=2)
btnNuevaPartida.grid(row=5,column=1)

btnNuevaPartida.config(state="disabled")

ventana.mainloop()