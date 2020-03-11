import threading
import time
import datetime
import re

lectura=""
#class Archivo(threading.Thread,archivo):
 #   def __init__(self):
  #      threading.Thread.__init__(self)   #Define que será un hilo
   # def run(self):
    #    try:
     #       file = open()
def leerArchivo(archivo):
    global lectura
    nombre = threading.current_thread().getName()
    print("Soy el hilo ",nombre)
    print("Abro el archivo: ",archivo)
    try:
        file = open(archivo, "r")
        lectura = file.read()
        #print(lectura)
        return(lectura)
    except EOFError:
        print("No se pudo leer el arhivo")
def buscarPatron(expresion):
    global lectura
    nombre = threading.current_thread().getName()
    print("Soy el hilo ",nombre)
    print("Calculo la expresion regular: ",expresion)
    lista=re.findall(expresion,lectura)
    print(lista)
    return lista

tiempo_ini = datetime.datetime.now()
mi_archivo = "datosReal.txt"

expresionR1="Frequencies\s*--\s*(\d+\.\d+)\s+(\d+\.\d+)\s*(\d+\.\d+)"
expresionR2="Rot. str.\s+--\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)"
expresionR3="Sum of electronic and thermal Enthalpies=\s+(-?\d+.\d+)"

hiloArchivo = threading.Thread(target=leerArchivo,args=(mi_archivo,))
hiloPatronTemperatura = threading.Thread(target=buscarPatron,args=(expresionR1,))
hilloEntalpia = threading.Thread(target=buscarPatron,args=(expresionR2,))
hiloRot = threading.Thread(target=buscarPatron,args=(expresionR3,))

hiloArchivo.start()
hiloArchivo.join()
hiloPatronTemperatura.start()
hilloEntalpia.start()
hiloRot.start()
hiloPatronTemperatura.join()
hilloEntalpia.join()
hiloRot.join()

tiempo_fin = datetime.datetime.now()
leerArchivo(mi_archivo)
print("Tiempo transcurrido "+str(tiempo_fin.second-tiempo_ini.second))
print("Terminó el programa")
#leerArchivo("datosReal.txt")       