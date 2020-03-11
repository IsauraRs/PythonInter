from tkinter import *
#import tkinter 


raiz = Tk()
miFrame = Frame()
raiz.title("Ventana pruebas")
raiz.config(bg="black") #Backgroud negro
raiz.config(cursor="pirate")
raiz.config(relief="groove")
#miFrame.config(bg="red",width=1200,height=600)
miFrame.pack()
miFrame.config(relief="groove")
minombre = StringVar() #Cadena de caracteres
miapellido =StringVar()
micorreo = StringVar()
tuapellido = StringVar()
pantalla=Text(miFrame, width=20, height=20)

#--------Todos los cuadros---------#
cuadroNombre = Entry(miFrame, textvariable=minombre)


cuadroNombre.grid(row=1, column=2,padx=10,pady=10)
cuadroApellido = Entry(miFrame, textvariable=miapellido)
cuadroApellido.grid(row=2, column=2,padx=10,pady=10)
cuadroCorreo = Entry(miFrame,textvariable=micorreo)
cuadroCorreo.grid(row=3, column=2,padx=10,pady=10)
cuadroTuApellido = Entry(miFrame, textvariable=tuapellido)
cuadroTuApellido.grid(row=4, column=2,padx=10,pady=10)


#--------Todos los label---------#

nombreLabel = Label(miFrame, text="Nombre", padx=10,pady=10)
nombreLabel.grid(row=1,column=1,padx=10,pady=10)
apellidoLabel = Label(miFrame, text="Apellido", padx=10,pady=10)
apellidoLabel.grid(row=2,column=1,padx=10,pady=10)
correoLabel = Label(miFrame, text="Correo", padx=10,pady=10)
correoLabel.grid(row=3,column=1,padx=10,pady=10)
tuapellidoLabel = Label(miFrame, text="Tu Apellido es", padx=10,pady=10)
tuapellidoLabel.grid(row=4,column=1,padx=10,pady=10)
def codigoBoton():
	minombre.set("Alejandro")
	micorreo.set("gabrielos307@gmail.com")
	variable = miapellido.get()
	tuapellido.set(variable)
buttonEnvio = Button(miFrame,text="Enviar", command=codigoBoton)
buttonEnvio.grid(row=5,column=1)
raiz.mainloop() #CIclo loop para ejecucion