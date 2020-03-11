import csv

with open('calificaciones.csv') as archivo:
    contenido= csv.reader (archivo,delimiter=":")
    for fila in contenido:
        print(fila[1])



