
import socket
import sys

host = sys.argv[1] if len(sys.argv) >= 2 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) >= 3 else 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((host, puerto))
    print(f"Conectado a {host}:{puerto}")

    for i in range(5):
        c.sendall(b"ABCDE")   
        print(f"Enviado {i+1}: ABCDE")

    c.sendall(b"FINAL")
    print("Enviado: FINAL")

print("Cliente terminado")
