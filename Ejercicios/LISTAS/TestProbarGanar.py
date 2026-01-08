from cartasUtil import calcularProbabilidadGanar
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def fnCalcularProbabilidad():
    probabilidad=calcularProbabilidadGanar(cartas,cartaMenor,cartaMayor)
    messagebox.showinfo(title="IMPORTANTE", message=f"Tienen el {probabilidad}% de probabilidad de ganar.")
cartaMenor="19-7-T-7"
cartaMayor="49-K-N-13"
cartaMenor2="14-4-N-4"
cartaMenor3="45-Q-T-13"

cartas={
    "40-J-D-11",
	"48-K-D-13",
	"4-2-D-2",
	"15-4-T-4",
	"8-3-D-3",
    "35-9-T-9",
	"29-8-N-8",
    "1-A-N-1",
	"37-10-N-10",
    "17-5-T-5",
    "19-5-N-5",
}

probabilidad1=calcularProbabilidadGanar(cartas,cartaMenor,cartaMayor)
print(f"PROBABILIDAD 1: {probabilidad1}%")
probabilidad2=calcularProbabilidadGanar(cartas,cartaMenor2,cartaMayor)
print(f"PROBABILIDAD 2: {probabilidad2}%")
probabilidad3=calcularProbabilidadGanar(cartas,cartaMenor3,cartaMayor)
print(f"PROBABILIDAD 2: {probabilidad3}%")

ventana=Tk()
ventana.geometry("200x200")
ventana.title("PROBABILIDAD")

btnBuscar=ttk.Button(text="PROBABILIDAD",width=20, command=fnCalcularProbabilidad)
btnBuscar.grid(row=3,column=4)

ventana.mainloop()