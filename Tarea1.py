class ErrorNoEsMultiplo(Exception):
    def __init__(self,valor):
        self.valorError = valor
    def __str__(self):
        print("Los números que ingresó no son múltiplos ", self.valorError)


def menu():

    v=0
    while v ==0:
        try:
            o= int(input("Qué desea hacer? \n1.-Sumar \n2.-Restar \n3.-Multiplicar \n4.-Dividir \n5.-Es múltiplo? "))

            if o == 1:
                try:
                    x= int(input("Ingrese el primer número: "))
                    y= int(input("Ingrese el segundo número: "))
                    z = x + y
                except ValueError:
                    print("Debe ingresar un número")
                else:
                    v=1    
                    print("El resultado de la suma es: ",z)

            elif o == 2:
                try:
                    x= int(input("Ingrese el primer número: "))
                    y= int(input("Ingrese el segundo número: "))
                    z = x - y
                except ValueError:
                    print("Debe ingresar un número")
                else:
                    v=1    
                    print("El resultado de la resta es: ",z)
            elif o == 3:
                try:
                    x= int(input("Ingrese el primer número: "))
                    y= int(input("Ingrese el segundo número: "))
                    z = x * y
                except ValueError:
                    print("Debe ingresar un número")    
                else:
                    v=1    
                    print("El resultado de la multiplicación es: ",z)
            if o == 4:
                try:
                    x= int(input("Ingrese el primer número: "))
                    y= int(input("Ingrese el segundo número: "))
                    z = x / y
                except ValueError:
                    print("Debe ingresar un número") 
                except ZeroDivisionError:
                    print("No se puede dividir entre cero")   
                else:
                    v=1    
                    print("El resultado de la división es: ",z)
            if o == 5:
                try:
                    print("El primer número será calculado como múltiplo del segundo")
                    x= int(input("Ingrese el primer número: "))
                    y= int(input("Ingrese el segundo número: "))
                    z = x%y
                    if z != 0:
                        raise ErrorNoEsMultiplo(z)
                        exit()
                except ValueError: 
                    print("Debe ingresar un número")
                else:
                    print("Son múltiplos") 




        except ValueError:
            print("Debe ingresar un número")   
print(menu())            