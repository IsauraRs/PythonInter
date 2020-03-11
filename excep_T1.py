class ErrorNoEsMultiplo(Exception):
    def __init__(self,valor):
        self.valorError = valor
    def __str__(self):
        print("Los números que ingresó no son múltiplos ", self.valorError)
