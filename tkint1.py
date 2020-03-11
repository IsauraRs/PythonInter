from tkinter import *

raiz = Tk()
miFrame = Frame()

raiz.title("Ventana pruebas")
raiz.config(bg="black") #Background negro
raiz.config(cursor="pirate")
raiz.config(relief="groove")

miFrame.config(bg="red",width=1200,height=600)
miFrame.pack()
miFrame.config(relief="groove")

miNombre = StringVar() #Cadena de caracteres que se ingresa
miApellido = StringVar()
miCorreo = StringVar()
tuApellido = StringVar()

pantalla=Text(miFrame,width=20,height=20)

cuadroNombre= Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=2,padx=10, pady=10)

cuadroApellido= Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=2,column=2,padx=10, pady=10)

cuadroCorreo= Entry(miFrame,textvariable=miCorreo)
cuadroCorreo.grid(row=3,column=2,padx=10, pady=10)

cuadroTuapellido= Entry(miFrame,textvariable=tuApellido)
cuadroTuapellido.grid(row=5,column=2,padx=10, pady=10)


nombreLabel = Label(miFrame, text="Nombre",padx=10,pady=10)
nombreLabel.grid(row=1,column=1,padx=10,pady=10)

apellidoLabel = Label(miFrame, text="Apellido",padx=10,pady=10)
apellidoLabel.grid(row=2,column=1,padx=10,pady=10)

correoLabel = Label(miFrame, text="Correo",padx=10,pady=10)
correoLabel.grid(row=3,column=1,padx=10,pady=10)

tuapellidoLabel = Label(miFrame, text="Tu apellido es: ",padx=10,pady=10)
tuapellidoLabel.grid(row=5,column=1,padx=10,pady=10)

def codigoBoton():
    miNombre.set("Isaura")
    miCorreo.set("isaura.rs29@gmail.com")
    var=miApellido.get()
    tuApellido.set(var)



buttonEnvio = Button(miFrame,text="Enviar", command=codigoBoton) #command: acción que va a ejecutar
buttonEnvio.grid(row=4,column=1,padx=10,pady=10)
#buttonEnvio.pack()



#pantalla = Entry(miFrame)


raiz.mainloop() #Ciclo loop para ejecución