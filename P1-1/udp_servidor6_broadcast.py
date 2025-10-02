import socket

PORT = 12345
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('', PORT))

print(f"Servidor HOLA escuchando en el puerto {PORT}...")

while True:
    data, addr = s.recvfrom(BUFFER_SIZE)
    mensaje = data.decode().strip()
    print(f"Recibido '{mensaje}' de {addr}")

    if mensaje == "BUSCANDO HOLA":
        s.sendto(b"IMPLEMENTO HOLA", addr)
        print(f"Respondido a {addr} con 'IMPLEMENTO HOLA'")
    elif mensaje == "HOLA":
        respuesta = f"HOLA: {addr[0]}"
        s.sendto(respuesta.encode(), addr)
        print(f"Respondido a {addr} con '{respuesta}'")