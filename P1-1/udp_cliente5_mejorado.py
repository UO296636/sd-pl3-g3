import socket
import sys

host = "localhost"
puerto = 9999

if len(sys.argv) > 1:
    host = sys.argv[1]
if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2.0)

print(f"Cliente UDP mejorado hacia {host}:{puerto}...")
contador = 1
while True:
    mensaje = input("> ")
    if mensaje == "FIN":
        break

    mensaje_numerado = f"{contador}: {mensaje}"
    sock.sendto(mensaje_numerado.encode(), (host, puerto))

    try:
        data, _ = sock.recvfrom(1024)
        respuesta = data.decode()
        print(f"Confirmación recibida: {respuesta}")

        # Verificamos que el identificador coincide
        if not respuesta.startswith(str(contador)):
            print("Confirmación recibida no corresponde al mensaje enviado")
    except socket.timeout:
        print("No se recibió confirmación")

    contador += 1

sock.close()
