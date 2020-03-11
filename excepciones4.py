def division(x,y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    else:
        print("Resultado: ",resultado)
    finally:
        print("Esto se hizo en una función")

print("Intento 1")
division(9,3)
print("Intento 2")                     
division(9,0)
print("Intento 3")
division(8,2)
