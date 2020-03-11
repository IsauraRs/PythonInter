import csv
from tkinter import *
from tkinter import messagebox, ttk
from random import randint
import proyb as dato

import sqlite3
con= sqlite3.connect('baseProyecto.db')
cursor = con.cursor()

#from proyv2 import botonGuarda, mandardatos
lista=[]

class Menu():
    #u = ""
    #c = ""
    #r = 0
    def __init__(self):

        self.raiz =Tk()
        self.raiz.geometry("300x200")
        self.raiz.title("Ventana principal")
        
        #botones
        boton_rol1 = Button(self.raiz, text='Rol 1', command = self.rol1).pack()
        boton_rol2 = Button(self.raiz, text='Rol 2', command = self.rol2).pack()
        boton_registrarse = Button(self.raiz, text='Registrarse', command = self.registrarse).pack()
        boton_salida = Button(self.raiz, text='Salida', command = self.raiz.destroy).pack()
        self.raiz.mainloop()

    def acepta(self):
        self.u=self.vaU.get()
        self.c=self.vaC.get()
        self.r=self.vaR.get()

        if re.findall('^[A-Z]{1}(.|\s|\S)+[0-9]$',self.c):
            try:
                insert_tabla(self.u,self.c,self.r)
                print("Correcto")
                print(self.n)    
                messagebox.showinfo(message="Agregado con exito", title="Exito!!!")
                #print(self.u);print(self.c);print(self.r)
            except:
                messagebox.showinfo(message="algo fallo", title="Error!!!") 
        else:
            messagebox.showinfo(message="No cumple con el formato", title="Error!!!")          
            print("No cumple")
            #print(self.u); print(self.c); print(self.r)

    def acceder(self):
        self.u1 = self.us.get()
        self.c2 = self.pw.get()
        self.a = self.na.get()
        
        if re.findall("listas",self.a):
            with open("listas2.csv",'a+') as l:
                print(l.read())
            with open("listas2.csv","a+") as f:
                messagebox.showinfo(message="Agregando datos", title="Exito!!!")
                reader = csv.reader(open('listas2.csv','r'),delimiter=',')
                for row in reader:
                    dato.insert_tabla_alu(row[0], row[1], row[2], row[3],row[4])
                messagebox.showinfo(message="Datos agregados", title="Exito!!!") 
        else:
            messagebox.showinfo(message="El archivo no existe o no se encuentra en el directorio", title="Error!!!")


        
    

    def rol1(self):
        self.rol1v = Toplevel()
        self.rol1v.title("Rol 1")
        self.us = StringVar()
        self.pw = StringVar()
        self.na = StringVar()

        usLabel = Label(self.rol1v, text="Usuario")
        usLabel.grid(row=1,column=5,padx=10,pady=10)
        
        usR = Entry(self.rol1v)
        usR.config(textvariable=self.us)
        usR.grid(row=1,column=2,padx=10,pady=10)

        pwrdLabel = Label(self.rol1v, text="Contraseña")
        pwrdLabel.grid(row=2,column=5,padx=10,pady=10)

        pwrdR = Entry(self.rol1v)
        pwrdR.config(textvariable=self.pw)
        pwrdR.grid(row=2,column=2,padx=10,pady=10)

        arLabel = Label(self.rol1v,text="Nombre del archivo")
        arLabel.grid(row=3,column=5,padx=10,pady=10)

        arR = Entry(self.rol1v)
        arR.config(textvariable=self.na)
        arR.grid(row=3,column=2,padx=10,pady=10)

        boton_ingresar = Button(self.rol1v, text='Ingresar', command = self.acceder)
        boton_ingresar.grid(row=4,column=2,padx=10,pady=10)



        #pass

    def rol22(self):
        self.rol2v2 = Toplevel()
        self.rol2v2.title("Opciones")

        boton_ingr = Button(self.rol2v2, text='Ingresar', command = self.ingresa2).pack()
        boton_rol2 = Button(self.rol2v2, text='Dar de baja', command = self.baja).pack()
        boton_registrarse = Button(self.rol2v2, text='Actualizar', command = self.actualiza).pack()
        boton_salida = Button(self.rol2v2, text='Salida', command = self.raiz.destroy).pack()

    def sS(self):
        self.saveStudent = Toplevel()
        self.saveStudent.title("Guardar estudiante")

    def guardar(self):
        self.nombre = self.name.get()
        self.apel = self.lastName.get()
        self.cnta = dato.aleaotario()
        self.edad = self.age.get()
        self.correo = self.mail.get()
        dato.insert_tabla_alu(self.cnta, self.nombre,self.apel,self.correo,self.edad)
        print("Ya")
    
    


    def ingresa2(self):
        self.ingresa22 = Toplevel()
        self.ingresa22.title("Ingresar")
        
        self.nc2 = IntVar()
        self.name = StringVar()
        self.lastName = StringVar()
        self.age = IntVar()
        self.mail = StringVar()

        numeroCuentaLabel = Label(self.ingresa22,text="Número de cuenta")
        numeroCuentaLabel.grid(row=1,column=5,padx=10,pady=10)
        boton_cuenta = Button(self.ingresa22, text='Generar número de cuenta', command = dato.aleaotario)
        boton_cuenta.grid(row=1,column=2,padx=10,pady=10)




        nombreLabel = Label(self.ingresa22,text="Nombre")
        nombreLabel.grid(row=2,column=5,padx=10,pady=10)

        nombreN = Entry(self.ingresa22)
        nombreN.config(textvariable=self.name)
        nombreN.grid(row=2,column=2,padx=10,pady=10)

        apellidosLabel = Label(self.ingresa22, text="Apellidos")
        apellidosLabel.grid(row=3,column=5,padx=10,pady=10)

        apellidos=Entry(self.ingresa22)
        apellidos.config(textvariable=self.lastName)
        apellidos.grid(row=3,column=2,padx=10,pady=10)

        correoLabel = Label(self.ingresa22, text="Correo")
        correoLabel.grid(row=4,column=5,padx=10,pady=10)

        correo=Entry(self.ingresa22)
        correo.config(textvariable=self.mail)
        correo.grid(row=4,column=2,padx=10,pady=10)

        edadLabel = Label(self.ingresa22, text="Edad")
        edadLabel.grid(row=5,column=5,padx=10,pady=10)

        edad=Entry(self.ingresa22)
        edad.config(textvariable=self.age)
        edad.grid(row=5,column=2,padx=10,pady=10)

        boton_salvar = Button(self.ingresa22, text='Guardar', command = self.guardar)
        boton_salvar.grid(row=6,column=5,padx=10,pady=10)

    def delete(self):
        self.cn = self.cuenta1.get()
        dato.eliminar(int(self.cn)) 
        print("Listo")   


    def baja(self):
        self.baja1 = Toplevel()
        self.baja1.title("Dar de baja")
        self.cuenta1 = IntVar()
        ######
        ######
        numeroCuentaLabel = Label(self.baja1,text="Numero de cuenta")
        numeroCuentaLabel.grid(row=1,column=5,padx=10,pady=10)

        numeroCuenta = Entry(self.baja1)
        numeroCuenta.config(textvariable=self.cuenta1)
        numeroCuenta.grid(row=1,column=2,padx=10,pady=10)

        boton_baja = Button(self.baja1, text='Dar de baja', command = self.delete)
        boton_baja.grid(row=4,column=5,padx=10,pady=10)
        boton_lista = Button(self.baja1, text='Listar', command = dato.consultas)
        boton_lista.grid(row=5,column=5,padx=10,pady=10)

    def act(self):
        self.ca = self.campo.get()
        self.co = self.count.get()
        self.vn2 = self.valN2.get()
        self.vn3 = self.valN3.get()
        self.vn4 = self.valN4.get()

        dato.actualizar(self.ca,self.vn2,self.vn3,self.vn4,self.co)    
        print("Listo")

    def actualiza(self):
        self.actualiza1 = Toplevel()
        self.actualiza1.title("Actualizar") 
        self.campo = StringVar()
        self.count = IntVar()
        self.valN2 = StringVar()
        self.valN3 = StringVar()
        self.valN4 = StringVar()

        campoLabel = Label(self.actualiza1,text="Nombre")
        campoLabel.grid(row=1,column=5,padx=10,pady=10)

        campo = Entry(self.actualiza1)
        campo.config(textvariable=self.campo)
        campo.grid(row=1,column=2,padx=10,pady=10)

        campo2Label = Label(self.actualiza1,text="Apellidos")
        campo2Label.grid(row=2,column=5,padx=10,pady=10)

        campo2 = Entry(self.actualiza1)
        campo2.config(textvariable=self.valN2)
        campo2.grid(row=2,column=2,padx=10,pady=10)

        campo3Label = Label(self.actualiza1,text="Correo")
        campo3Label.grid(row=3,column=5,padx=10,pady=10)

        campo3 = Entry(self.actualiza1)
        campo3.config(textvariable=self.valN3)
        campo3.grid(row=3,column=2,padx=10,pady=10)

        campo4Label = Label(self.actualiza1,text="Edad")
        campo4Label.grid(row=4,column=5,padx=10,pady=10)

        campo4 = Entry(self.actualiza1)
        campo4.config(textvariable=self.valN4)
        campo4.grid(row=4,column=2,padx=10,pady=10)

        cuentaLabel = Label(self.actualiza1,text="Número de cuenta del alumno")
        cuentaLabel.grid(row=5,column=5,padx=10,pady=10)

        cuenta = Entry(self.actualiza1)
        cuenta.config(textvariable=self.count)
        cuenta.grid(row=5,column=2,padx=10,pady=10)

        boton_en = Button(self.actualiza1, text='Actualizar', command = self.act)
        boton_en.grid(row=6,column=5,padx=10,pady=10)
        



    def rol2(self):
        self.rol2v = Toplevel()
        self.rol2v.title("Rol 2")
        self.usr = StringVar()
        self.paswrd = StringVar()

        user1Label = Label(self.rol2v,text="Usuario")
        user1Label.grid(row=1,column=5,padx=10,pady=10)

        userN1 = Entry(self.rol2v)
        userN1.config(textvariable=self.usr)
        userN1.grid(row=1,column=2,padx=10,pady=10)

        password1Label = Label(self.rol2v, text="Contraseña")
        password1Label.grid(row=2,column=5,padx=10,pady=10)

        passW1=Entry(self.rol2v)
        passW1.config(textvariable=self.paswrd)
        passW1.grid(row=2,column=2,padx=10,pady=10)

        boton_en = Button(self.rol2v, text='Ingresar', command = self.rol22)
        boton_en.grid(row=4,column=5,padx=10,pady=10)
        

    def registrarse(self):
        self.registrarsev = Toplevel()
        self.registrarsev.title("Registrarse")
        self.vaU = StringVar()
        self.vaC = StringVar()
        self.vaR = IntVar()

        #self.ent = Frame(self.registrarsev)
        #self.ent.pack()
        userLabel = Label(self.registrarsev,text="Usuario")
        userLabel.grid(row=1,column=5,padx=10,pady=10)

        userN = Entry(self.registrarsev)
        userN.config(textvariable=self.vaU)
        userN.grid(row=1,column=2,padx=10,pady=10)

        passwordLabel = Label(self.registrarsev, text="Contraseña")
        passwordLabel.grid(row=2,column=5,padx=10,pady=10)

        passW=Entry(self.registrarsev)
        passW.config(textvariable=self.vaC)
        passW.grid(row=2,column=2,padx=10,pady=10)

        rolLabel = Label(self.registrarsev,text = "Rol")
        rolLabel.grid(row=3,column=5,padx=10,pady=10)
        rol=Entry(self.registrarsev)
        rol.config(textvariable=self.vaR)
        rol.grid(row=3,column=2,padx=10,pady=10)

        boton_guardar = Button(self.registrarsev, text='Guardar', command = self.acepta)
        boton_guardar.grid(row=4,column=5,padx=10,pady=10)


def main():
    dato.crea_tab()
    dato.crea_tabalm()
    aplicacion = Menu()
    return 0

if __name__  == "__main__":
	main()