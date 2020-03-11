import socket
recvIP= input("Ingresa la IP con la cual te quieres conectar: ")
ss= socket.socket()
ss.bind((recvIP,9000))
ss.listen(1)
conn ,addr = ss.accept()
print("Iniciando el servidor")
print("Cliente conectado desde: ", addr[0], ":", addr[1])

while True:
    recibido= conn.recv(5000).decode()
    if recibido == "adiós":
        break
    print("Client >> ", recibido)
    conn.send(input("Ingresa tu mensaje >> ").encode())

print("Se ha terminado la conexión")
ss.close()
    