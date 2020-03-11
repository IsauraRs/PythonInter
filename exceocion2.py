bandera = 0
while bandera == 0:
    try:
        x = int(input("Inserte un número: "))
        y =int(input("Inserte otro número: "))
        bandera = 1
        z = x + y
    except ValueError:    
        print("Debe ingresar un número") 
    else:
        print("La suma es: ",z)



