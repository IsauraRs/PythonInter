import re
import time
import datetime
import threading
lectura = ""

def leerArchivo(archivo):
	global lectura
	nombre = threading.current_thread().getName()	
	print("Soy el hilo ",nombre)
	print("Abro el archivo: ",archivo)
	try:
		file = open(archivo, "r")
		lectura = file.read()
		print(type(lectura)) #Es string??
	
	except EOFError:
		print("No se pudo abri el archivo")

def buscarPatron(expresion):
	global lectura
	nombre = threading.current_thread().getName()	
	print("Soy el hilo ",nombre)
	print("Calculo la expresion regular: ",expresion)
	lista = re.findall(expresion, lectura)
	print(lista)
	return lista

tiempo_ini = datetime.datetime.now()
mi_archivo = "datosReal.txt"

expresionR1="Frequencies\s*--\s*(\d+\.\d+)\s+(\d+\.\d+)\s*(\d+\.\d+)"
expresionR2="Rot. str.\s+--\s+(-?\d+.\d+)\s+(-?\d+.\d+)\s+(-?\d+.\d+)"
expresionR3="Sum of electronic and thermal Enthalpies=\s+(-?\d+.\d+)"	
hiloArchivo = threading.Thread(target=leerArchivo, args=(mi_archivo,))
hiloPatronTemperatura = threading.Thread(target=buscarPatron, args=(expresionR1,))
hiloEntalpia = threading.Thread(target=buscarPatron, args=(expresionR2,))
hiloRot = threading.Thread(target=buscarPatron, args=(expresionR3,))
hiloArchivo.start()
hiloArchivo.join()
hiloPatronTemperatura.start()
hiloEntalpia.start()
hiloRot.start()
hiloPatronTemperatura.join()
hiloEntalpia.join()
hiloRot.join()

tiempo_fin = datetime.datetime.now()
print("Tiempo transcurrido "+str(tiempo_fin.second-tiempo_ini.second))
print("Termino el programa")