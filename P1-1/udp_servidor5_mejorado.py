import socket
import sys
import random

puerto = 9999
if len(sys.argv) > 1:
    puerto = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", puerto))

print(f"Servidor UDP mejorado escuchando en el puerto {puerto}...")

while True:
    data, addr = sock.recvfrom(1024)

    if random.randint(0, 1) == 0:
        print("Simulando paquete perdido")
    else:
        mensaje = data.decode()
        print(f"Mensaje recibido: {mensaje} desde {addr}")

        # Se asume que el datagrama tiene el formato "id: mensaje"
        partes = mensaje.split(":", 1)
        if len(partes) > 1:
            identificador = partes[0].strip()
            # El servidor responde con el mismo identificador + OK
            sock.sendto(f"{identificador}: OK".encode(), addr)
