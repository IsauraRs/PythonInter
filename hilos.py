import threading
import datetime


def contador():
    nombre = threading.current_thread().getName()
    print("Soy el hilo",nombre)
    lista1 = []
    for i in range(1,4999999):
        lista1.append(i)
    return lista1 

def contador1(lista1):
    nombre = threading.current_thread().getName()
    print("Soy el hilo" + nombre)
    lista2 = []
    for i in range(5000000,10000000):
        lista2.append(i)
    return lista2    

def sumador(lista1,lista2):
    resultado = []
    for i in range(0,4999999):
        suma=lista1[i] + lista2[i] 
        resultado.append(suma)
        print([resultado[i]])


tiempo_ini = datetime.datetime.now()
hilo1 = threading.Thread(target=contador,args=(contador(),))
hilo2=threading.Thread(target=contador, args=(contador(),))
hilo3=threading.Thread(target=sumador, args=(contador(),contador()),)
hilo1.start()
hilo2.start()
hilo3.start()
hilo1.join()
hilo2.join()
hilo3.join()
tiempo_fin = datetime.datetime.now()
print("Tiempo transcurrido " +str(tiempo_fin.second-tiempo_ini.second))
print("Terminó el programa")