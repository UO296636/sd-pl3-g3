import socket
import sys

puerto = int(sys.argv[1]) if len(sys.argv) >= 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)
print(f"Servidor escuchando en el puerto {puerto}...")

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print(f"Nuevo cliente conectado desde {origen[0]}:{origen[1]}")

    while True:
        datos = sd.recv(1024)
        print(f"Recibido: {repr(datos)}")

        if datos == b"":
            print("Cliente cerró la conexión")
            sd.close()
            break

        respuesta = datos[::-1]
        print(f"Enviando: {repr(respuesta)}")
        sd.sendall(respuesta)
