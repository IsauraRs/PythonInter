import threading

def funcion():
    nombre = threading.current_thread().getName()
    print("Soy el hilo",nombre)
    print("Hola")

hilos = []

for i in range(10):
    hilos.append(threading.Thread(target=funcion))
    hilos[i].start()
    hilos[i].join()
