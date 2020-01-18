class Abuelo():
    def __init__(self):
        print("Soy el abuelo")
    def Leer(self):
        print("Se leer")

class Abuela():
    def __init__(self):
        print("Soy la abuela")
    def Escribir(self):
        print("Se escribir")

class Nieto(Abuelo,Abuela):
    def __init__(self):
        print("Soy el nieto")
        
    def Pintar(self):
        print("Se pintar")

isa = Nieto()
isa.Leer()
isa.Escribir()
isa.Pintar()