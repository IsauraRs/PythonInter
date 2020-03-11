class ErrorDivisionOcho(Exception):
    def __init__(self,valor):
        self.valor = valor
    def __str__(self):
        print("Error dividir entre ", self.valor)
try: 
    x= int(input("Ingrese un número: "))

    if x == 8:
        raise ErrorDivisionOcho(x)
        exit()
except:
    print("Esto no es posible")        
else:
    print(10/x)
