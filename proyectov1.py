from tkinter import*
from proyv2 import *

def cerrar():
    global raiz
    raiz.destroy()


def guardaCont():
    print('Guardado',vaU.get())
    vaU.set(' ')


def guardaUs():
    print('Guardado',vaC.get())
    vaC.set(' ')

def guardaRol():
    print('Guardado',vaR.get())
    vaR.set(' ')



raiz = Tk()

var1 = IntVar()
chk1 = Checkbutton(raiz, text='Rol1', variable=var1)
chk1.pack()


var2 = IntVar()
chk2 = Checkbutton(raiz, text='Rol2', variable=var2)
chk2.pack()


var3 = IntVar()
chk3 = Checkbutton(raiz, text='Registrarse', variable=var3)
chk3.pack()


var4 = IntVar()
chk4 = Checkbutton(raiz,text='Salir', variable=var4)
chk4.pack()



def darEstados():
    if var1.get()==1:
        print("Rol1")
    elif var2.get()==1:
        print("Rol2")
    elif var3.get()==1:
        cerrar()
        ventana = Toplevel()
        #regi()
        #botonGuarda()

    elif var4.get()==1:
        print("Salir")
        cerrar()



Button(raiz, text='Seleccionar', command=darEstados).pack()

raiz.mainloop()

    
