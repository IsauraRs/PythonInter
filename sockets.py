import socket
recvIp= input("Ingresa la IP con la que te quieres conectar: ")
s= socket.socket()
s.connect((recvIp,9000))
while True:
	mensaje=input("Ingresa el mensaje1: ")
	s.send(mensaje.encode())
	if mensaje=="adiós":
		break
	respuesta=s.recv(1024).decode()
	print("Respuesta del servidor: ", respuesta)

print("Conexión finalizada")

s.close()