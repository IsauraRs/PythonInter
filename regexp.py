#Se divide la expresion en la cantidad de elementos que hay, contando el símbolo, por ejemplo el de fecha se divide en 5: dd/mm/yyyy o dd-mm-yyyy: 
#([0-3][0-9]) se subdivide la expresión anterior ya que podría dar 32 o más, siendo incorrecto, por lo que queda: 
# ([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])(\/|-)(1|2)(1[8-9][0-9][0-9]20[0-2][0-9])
#Los primeros rangos evalúan del 01 al 29, el segundo, del 30 al 31, se escapa el caracter "/" para que sea leído como tal, el siguiente rango es 
#para los meses, del 0 al 9 o el segundo del 1 al 2
#match siempre busca al inicio de la línea
import re
if re.match("Hola","hola"):
    print("Hizo match1")

if re.match(".ola","tola"):
    print("Hizo match2")

if re.match("python|jython|cython","cython"):
    print("Hizo match3")

if re.match("(p|c|j)ython","cyhton"):
    print("Hizo match4") 
    
if re.match("python+","pythonnnn"):
    print("Hizo match5")

if re.match("python*","pytho"):
    print("Hizo match6")
if re.match("python{3,8}","pythonnn"):
    print("Hizo match7")
if re.match("^http:$","http://google.com"):
    print("Hizo match8")                 
if re.match("python[0-9a-z]","pythonZ",re.IGNORECASE):
    print("Hizo match9")
