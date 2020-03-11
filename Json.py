import json
D={"Pedro":9, "Saul":5,"Mariana":10,"Julia":9}
J=json.dumps(D) #Convierte el archivo
print(J)
ND=json.loads(J) #Carga el objeto del método Json a uno de tipo python
ND= dict (ND)
print(ND)

with open("Diccionario.json","w") as f:
   json.dump(D,fp=f)  #json.dump(Informacion que se quiere almacenar(objeto),archivo en el que se almacenará)Para escribir información en archivo Json
with open ("Diccionario.json","r") as FILE:
   informacion= json.load(FILE)
   print(informacion.keys())