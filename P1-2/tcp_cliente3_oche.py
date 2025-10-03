import socket
import sys

host = sys.argv[1] if len(sys.argv) >= 2 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) >= 3 else 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((host, puerto))
    print(f"Conectado a {host}:{puerto}")

    lineas = [
        b"Hola mundo\r\n",
        b"Python TCP\r\n",
        b"12345\r\n"
    ]

    for linea in lineas:
        print(f"Enviando: {repr(linea)}")
        c.sendall(linea)

        respuesta = c.recv(1024)
        print(f"Recibido: {repr(respuesta)}")

print("Cliente terminado")
