import socket
import sys

puerto = 9999
if len(sys.argv) > 1:
    puerto = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", puerto))

print(f"Servidor UDP escuchando en el puerto {puerto}...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Mensaje recibido: {data.decode()} desde {addr}")
