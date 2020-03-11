class MatchError(Exception):
    def __str__(self):
        print("Cantidades de match insuficientes")
import re
texto = "El día de hoy aprenderemos expresiones regulares en python 3 python python "
cadena = "python"

print(re.findall(cadena,texto))
tam=len(re.findall(cadena,texto))

if tam < 4:
    raise MatchError()
    exit()
else: 
    print("Matches suficientes")


