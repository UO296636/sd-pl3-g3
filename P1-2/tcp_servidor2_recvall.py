import socket
import sys

puerto = int(sys.argv[1]) if len(sys.argv) >= 2 else 9999
TAM = 5

def recvall(sock, n: int) -> str | None:
    """
    Intenta recibir exactamente n bytes del socket.
    Devuelve un string (decodificado en ASCII) con los datos leídos,
    o None si la conexión se cierra antes de completar.
    """
    datos = bytearray()
    while len(datos) < n:
        bloque = sock.recv(n - len(datos))
        if not bloque:  
            return None
        datos.extend(bloque)
    return datos.decode("ascii")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen(5)
print(f"Servidor escuchando en el puerto {puerto}...")

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print(f"Nuevo cliente conectado desde {origen[0]}, {origen[1]}")

    continuar = True
    while continuar:
        datos = recvall(sd, TAM)
        if datos is None:
            print("Conexión cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False
        elif datos == "FINAL":
            print("Recibido mensaje de finalización")
            sd.close()
            continuar = False
        else:
            print(f"Recibido mensaje: {datos}")
