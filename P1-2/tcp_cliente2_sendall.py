
import socket
import sys

# Host y puerto desde CLI o localhost:9999 por defecto
host = sys.argv[1] if len(sys.argv) >= 2 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) >= 3 else 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect((host, puerto))
    print(f"Conectado a {host}:{puerto}")

    # Enviar 5 veces "ABCDE"
    for i in range(5):
        c.sendall(b"ABCDE")   # garantiza envío completo
        print(f"Enviado {i+1}: ABCDE")

    # Enviar "FINAL"
    c.sendall(b"FINAL")
    print("Enviado: FINAL")

print("Cliente terminado")
