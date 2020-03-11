from tkinter import*
root = Tk()

ent = Frame()
#boton = Button(root ,text='Hola')

ent.pack()

var=StringVar()
var2=StringVar()

cuadro1 = Entry(ent,textvariable=var)
cuadro1.pack()
cuadro2 = Entry(ent,textvariable=var2)
cuadro2.pack()
def mandar():
    print('Recibido: ', var.get())
    var.set('')
    
#boton.config(command=mandar)
#ent.pack(side=LEFT)
#boton.pack(side=RIGHT)    
root.mainloop()