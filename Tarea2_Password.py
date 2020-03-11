class PasswordSystemError(Exception):
    def __init__ (self,valor):
        self.valor3= valor
    def __str__ (self):
        print("Contraseña incorrecta",self.valor3)

m=int(input("Qué desea hacer? \n1.- Ingresar contraseña manualmente \n2.-Ingresar contraseña através de archivo \n"))
n= 12345
if m==1:
    try:
        u=input("Ingrese su nombre de usuario: ")
        p=int(input("Ingrese su contraseña: ")) 
        if p != 12345:
            raise PasswordSystemError(p) 
            exit()
        else:
            print("bienvenido")
    except PasswordSystemError as p:
        print("Fallo la autenticacion")
        print("La contraseña no es: ",p.valor3)
        print("La cintraseña es ", n)                         

if m==2:
    with open("contraseña.txt","a") as file:
        file.write("isaura.rs29@gmail.com \n12345abc")
    with open ("contraseña.txt","r") as c:
        print(c.read()) 
        print("Bienvenido") 

input("Contuna la ejecucion")