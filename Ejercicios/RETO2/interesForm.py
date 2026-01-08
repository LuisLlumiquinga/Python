from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from credito import calcularInteresSimple
from credito import calcularInteresCompuesto

def fnInteresSimple():
    limpiarError()
    monto=int(txtMonto.get())
    plazo=int(txtPlazo.get())
    tasa=int(txtTasa.get())

    errorMonto=False
    errorPlazo=False
    errorTasa=False

    if monto<1000 or monto>50000:
        lblErrorMonto.config(text="El monto debe estar entre 1000 y 50000")
        errorMonto=True
    
    if plazo<1 or plazo>15:
        lblErrorPlazo.config(text="El plazo debe estar entre 1 y 15 años")
        errorPlazo=True
    
    if tasa<3 or tasa>20:
        lblErrorTasa.config(text="La tasas debe estar entre 3 y 20 porciento")
        errorTasa=True

    if errorMonto==False and errorPlazo==False and errorTasa==False:
        interesSimple=calcularInteresSimple(monto, plazo, tasa)
        lblInteres.config(text=f"Invierte {monto}, a {plazo} años, con un interés simple del {tasa}% anual. Gana {interesSimple} de interés al cabo de los {plazo} años")
        errorMonto=False
        errorPlazo=False
        errorTasa=False


def fnInteresCompuesto():
    limpiarError()
    monto=int(txtMonto.get())
    plazo=int(txtPlazo.get())
    tasa=int(txtTasa.get())

    monto=int(txtMonto.get())
    plazo=int(txtPlazo.get())
    tasa=int(txtTasa.get())

    errorMonto=False
    errorPlazo=False
    errorTasa=False

    if monto<1000 or monto>50000:
        lblErrorMonto.config(text="El monto debe estar entre 1000 y 50000")
        errorMonto=True
    
    if plazo<1 or plazo>15:
        lblErrorPlazo.config(text="El plazo debe estar entre 1 y 15 años")
        errorPlazo=True
    
    if tasa<3 or tasa>20:
        lblErrorTasa.config(text="La tasas debe estar entre 3 y 20 porciento")
        errorTasa=True

    if errorMonto==False and errorPlazo==False and errorTasa==False:
        interesCompuesto=calcularInteresCompuesto(monto, plazo, tasa)
        lblInteres.config(text=f"Invierte {monto}, a {plazo} años, con un interés compuesto del {tasa}% anual. Gana {interesCompuesto} de interés al cabo de los {plazo} años")
        errorMonto=False
        errorPlazo=False
        errorTasa=False

def fnLimpiar():
    txtMonto.delete(0,END)
    txtPlazo.delete(0,END)
    txtTasa.delete(0,END)
    lblInteres.config(text="")

def limpiarError():
    lblErrorMonto.config(text="")
    lblErrorPlazo.config(text="")
    lblErrorTasa.config(text="")
    lblInteres.config(text="")

   # messagebox.showinfo(title="Interes Simple", message="Estudiante Guardado")
#GRAFICA
ventana=Tk()
ventana.title("PRESTAMO")
ventana.geometry("850x400")
tabControl=ttk.Notebook(ventana)


tabControl.pack(expand = 1, fill ="both") 
#TAB REGISTRO
frRegistro= Frame()
frRegistro.place(x=100,y=100)
lblMonto=ttk.Label(frRegistro,text="MONTO:")
lblPlazo=ttk.Label(frRegistro,text="PLAZO:")
lblTasa=ttk.Label(frRegistro,text="TASA:")

lblInteres=ttk.Label(frRegistro,foreground="blue")

txtMonto=ttk.Entry(frRegistro)
txtPlazo=ttk.Entry(frRegistro)
txtTasa=ttk.Entry(frRegistro)

lblErrorMonto=ttk.Label(frRegistro,text="",foreground="red")
lblErrorPlazo=ttk.Label(frRegistro,text="",foreground="red")
lblErrorTasa=ttk.Label(frRegistro,text="",foreground="red")

frBotones=Frame(frRegistro)
btnGuardar=ttk.Button(frBotones,text="CALCULAR SIMPLE",width=20, command=fnInteresSimple)
btnNuevo=ttk.Button(frBotones,text="CALCULAR COMPUESTO",width=20, command=fnInteresCompuesto)
btnLimpiar=ttk.Button(frBotones,text="LIMPIAR",width=20, command=fnLimpiar)

btnGuardar.grid(row=0,column=0,padx=10)
btnNuevo.grid(row=0,column=1,padx=10)
btnLimpiar.grid(row=0, column=2, padx=10)

lblMonto.grid(row=2,column=1,padx=30)
txtMonto.grid(row=2,column=2,pady=2)
lblErrorMonto.grid(row=2,column=3)
lblPlazo.grid(row=3,column=1,pady=2)
txtPlazo.grid(row=3,column=2)
lblErrorPlazo.grid(row=3,column=3)
lblTasa.grid(row=4,column=1,pady=2)
txtTasa.grid(row=4,column=2)
lblErrorTasa.grid(row=4,column=3)



lblInteres.grid(row=9,column=2)
frBotones.grid(row=10,column=0,columnspan=4,pady=10)

ventana.mainloop()


