try:
    x = int(input("Ingresa un número: "))
    y = 10/x
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Debes ingresar un número")
else: 
    print("La división es: ",y)
finally:
    print("Esto siempre se ejecuta")
print("Bye")
        


