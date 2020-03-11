import re
c=input("Ingrese la contraseña: ")


if re.findall('^[a-z]{3}[0-9]{2}([A-Z]|[a-z]){3}(.|\s|\S|\d){1}$',c):
    print(("Bienvenido"))

else:
    print("La contraseña no cumple con el formato requerido")