import re
instructores = ["Karina Flores","Alejandro Herrera","Héctor Cabello","Stephanie Cabello"]

for i in instructores:
    if re.findall('Cabello$',i):
        print(i)
    else:
        print("No hubo coincidencia")
