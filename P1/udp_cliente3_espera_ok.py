import socket
import sys

host = "localhost"
puerto = 9999

if len(sys.argv) > 1:
    host = sys.argv[1]
if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2.0)  # tiempo máximo de espera en segundos

print(f"Cliente UDP con espera de OK hacia {host}:{puerto}...")
contador = 1
while True:
    mensaje = input("> ")
    if mensaje == "FIN":
        break

    mensaje_numerado = f"{contador}: {mensaje}"
    sock.sendto(mensaje_numerado.encode(), (host, puerto))
    contador += 1

    try:
        data, _ = sock.recvfrom(1024)
        print(f"Confirmación recibida: {data.decode()}")
    except socket.timeout:
        print("⚠️ No se recibió confirmación (posible pérdida de paquete)")

sock.close()
