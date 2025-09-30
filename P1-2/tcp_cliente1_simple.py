# tcp_cliente1_simple.py
import socket
import sys

# Dirección y puerto por línea de comandos o valores por defecto
host = sys.argv[1] if len(sys.argv) >= 2 else "localhost"
puerto = int(sys.argv[2]) if len(sys.argv) >= 3 else 9999

# Crear socket TCP
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    c.connect((host, puerto))
    print(f"Conectado a {host}:{puerto}")

    # Enviar 5 veces "ABCDE"
    for i in range(5):
        c.sendall(b"ABCDE")
        print(f"Enviado {i+1}: ABCDE")

    # Enviar "FINAL"
    c.sendall(b"FINAL")
    print("Enviado mensaje FINAL")

finally:
    c.close()
    print("Socket cerrado")
