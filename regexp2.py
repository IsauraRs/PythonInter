import re
texto = "El día de hoy aprenderemos expresiones regulares en python 3"
cadena = "expresiones regulares"

isMatch = re.search(cadena,texto)

if isMatch is not None:
    print("Hizo match")
    print("El match inicia en: ", isMatch.start())
    print("El match termina en: ", isMatch.end())
    print("El match se hizo en: ", isMatch.span())
    print("El match fue: " , isMatch.group()) 

else:
    print("No hubo match")    