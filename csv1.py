import csv
listaQueGuarda=[]
for i in range (15):
    listaQueGuarda.append(["linea1","Linea2","Linea3","Linea4"])
    print(listaQueGuarda)

with open ("NuevoArchivo.csv","w") as f:
    escritura= csv.writer(f,delimiter=",")    
    for fila in listaQueGuarda 