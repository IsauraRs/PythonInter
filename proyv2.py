from tkinter import messagebox
#from proyb import *
import re
lista = []

def regi():
    raiz1=Tk()
    vaU = StringVar()
    vaC = StringVar()
    vaR = IntVar()
        
    u=vaU.get()
    c=vaC.get()
    r=vaR.get()
    ent = Frame()
    ent.pack()
    print("Registrarse")
    userN = Entry(ent,textvariable=vaU)
    userN.grid(row=1,column=2,padx=10,pady=10)
    passW=Entry(ent,textvariable=vaC)
    passW.grid(row=2,column=2,padx=10,pady=10)
    rol=Entry(ent,textvariable=vaR)
    rol.grid(row=3,column=2,padx=10,pady=10)
    userLabel = Label(ent,text="Usuario")
    userLabel.grid(row=1,column=5,padx=10,pady=10)
    passwordLabel = Label(ent,text="Contraseña")
    passwordLabel.grid(row=2,column=5,padx=10,pady=10)
    rolLabel = Label(ent,text = "Rol")
    rolLabel.grid(row=3,column=5,padx=10,pady=10)
    #botonReg=Button(raiz1, text='Registrar', command=reg)
    #botonReg.pack()

def mandardatos():
    pass
     
def botonGuarda(u,c,r):
    if re.findall('^[A-Z]{1}(.|\s|\S)+[0-9]$',c):
        print("Correcto")
        #insert_tabla(tup)
        #messagebox.showinfo(message="Agregado con exito", title="Exito!!!")
        
    else:
        #messagebox.showinfo(message="No cumple con el formato", title="Error!!!")          
        print("No cumple")


