import socket
import sys

host = "localhost"
puerto = 9999

if len(sys.argv) > 1:
    host = sys.argv[1]
if len(sys.argv) > 2:
    puerto = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Cliente UDP con reintentos hacia {host}:{puerto}...")
contador = 1
while True:
    mensaje = input("> ")
    if mensaje == "FIN":
        break

    mensaje_numerado = f"{contador}: {mensaje}"
    intentos = 0
    timeout = 1.0

    while True:
        try:
            sock.settimeout(timeout)
            sock.sendto(mensaje_numerado.encode(), (host, puerto))
            data, _ = sock.recvfrom(1024)
            print(f"Confirmación recibida: {data.decode()}")
            break
        except socket.timeout:
            intentos += 1
            print(f"⚠️ Timeout (intento {intentos}, espera {timeout:.1f}s)")

            timeout *= 2
            if timeout > 2.0:
                print("Puede que el servidor esté caído. Inténtelo más tarde")
                sock.close()
                sys.exit()

    contador += 1

sock.close()
