class ErrorDivisonOcho(Exception):
	def __init__(self,valor):
		self.valorError =valor

	def __str__(self):
		print("No se puede dividir entre ",self.valorError)


x = int(input("Ingresa un numero: "))

if x==8:
	raise ErrorDivisonOcho(x)
	exit()
else:
	print(10/x)