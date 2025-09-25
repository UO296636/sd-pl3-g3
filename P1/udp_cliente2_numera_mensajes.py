import socket
import sys

host = "localhost"
puerto = 9999

if len(sys.argv) > 1:
    host = sys.argv[1]
if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Cliente UDP numerando mensajes hacia {host}:{puerto}...")
contador = 1
while True:
    mensaje = input("> ")
    if mensaje == "FIN":
        break
    mensaje_numerado = f"{contador}: {mensaje}"
    sock.sendto(mensaje_numerado.encode(), (host, puerto))
    contador += 1

sock.close()
