with open("archivo1.txt","r") as a:
    #"""Lee el contenido del archivo en la consola Ejercicio1 """
    print(a.read())

with open ("archivo1.txt","a") as file: #"""Escribe en el archivo archivo1.txt las siguientes líneas Ejercicio2"""
    for i in range(2,10+1):
        file.write("linea " +str(i)+"\n")


    