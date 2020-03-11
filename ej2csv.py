import csv

with open('listas2.csv') as archivo:
	lectura = csv.reader(archivo)
	for fila in lectura:
		print(fila)

# Se crea una lista por fila

# Si los elementos no se separan con comas
"""
with open('calificaciones2.csv') as archivo:
	lectura = csv.reader(archivo, delimiter=':')
	for fila in lectura:
		print(fila)


# Para escribir a un archivo

lista = [1,2,3,4,"hola"]

with  open('calificaciones.csv') as arch1 ,open('archivo.csv', 'w') as arch2:
	lectura = csv.reader(arch1)
	escritura = csv.writer(arch2,delimiter = ':')
	for fila in lectura:
		escritura.writerow(fila)
        """