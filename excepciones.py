#Documentación de excepciones https://docs.python.org/3/library/exceptions.html
lista = [1,2,3,4]

#AttributeError
try:
    x=1
    x.atributo =10

except AttributeError:
    print("X no es un objeto y no tiene atributos")

#Index error
try: 
    print(lista[4])

except IndexError:
    print("Este índice no existe")

#Key error
dic={1:"Hola", 2:"Adiós"}
try:
    print(dic[3])
except KeyError:
    print("No existe esa llave")

