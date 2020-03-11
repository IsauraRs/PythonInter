from tkinter import*
import re

def cerrar():
    global raiz
    raiz.quit()


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
    #for variable in variables:
    if var1.get()==1:
        print("Rol1")
        #(variable.get(),end=' ')
    elif var2.get()==1:
        print("Rol2")
    elif var3.get()==1:
        raiz1=Tk()
        ent = Frame()
        ent.pack()

    
        print("Registrarse")
        cerrar()
        vaU = StringVar()
        
        u=vaU.get()
        vaC = StringVar()
        c=vaC.get()
        vaR = IntVar()
        r=vaR.get()
        
        
        userN = Entry(ent,textvariable=vaU)
        userN.grid(row=1,column=2,padx=10,pady=10)
        #Button(raiz,text='Guardar Usuario',command=guardaUs)
        #guardaUs()
        #root2=Tk()
        #ent2= Frame()
        passW=Entry(ent,textvariable=vaC)
        passW.grid(row=2,column=2,padx=10,pady=10)
        #Button(raiz,text='Guardar Constraseña',command=guardaCont)
        #guardaCont()
        #root3=Tk()
        #ent3= Frame()
        rol=Entry(ent,textvariable=vaR)
        rol.grid(row=3,column=2,padx=10,pady=10)
        
        #Button(raiz,text='Guardar Rol',command=guardaRol)

        userLabel = Label(ent,text="Usuario")
        userLabel.grid(row=1,column=5,padx=10,pady=10)
        passwordLabel = Label(ent,text="Contraseña")
        passwordLabel.grid(row=2,column=5,padx=10,pady=10)
        rolLabel = Label(ent,text = "Rol")
        rolLabel.grid(row=3,column=5,padx=10,pady=10)
        
        
        if re.findall('^[A-Z]{1}(.|\s|\S)+[0-9]$',c):
            crea_tab()
            datos = "INSERT INTO admin VALUES( " + u + c + r + ")"
            cursor.execute(datos)
            con.commit()
            cursor.execute("SELECT * FROM admin")   
        raiz1.mainloop()    
        

    elif var4.get()==1:
        print("Salir")



Button(raiz, text='Seleccionar', command=darEstados).pack()

raiz.mainloop()




