import json
n=input("Escriba un nombre: ")
a1=input("Escriba el primer apellido: ")
a2=input("Escripa el segundo apellido: ")
c=input("¿De qué color es? ")
fn=input("Ingrese la fecha de nacimiento: ")
cd=input("Ingrese la ciudad: ")
D={n:1,a1:2,a2:3,c:4,fn:5,cd:6}
#print(D.keys())
J=json.dumps(D)
print(J)
Ob=json.loads
for etiqueta in J:
   print("Nombre: ", etiqueta[n])
