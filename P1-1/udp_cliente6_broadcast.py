import socket
import sys
import time

# Parámetros por defecto
broadcast_ip = "255.255.255.255"
port = 12345
BUFFER_SIZE = 1024
TIMEOUT = 3

# Leer argumentos si se proporcionan
if len(sys.argv) >= 2:
    broadcast_ip = sys.argv[1]
if len(sys.argv) >= 3:
    port = int(sys.argv[2])

# Crear socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.settimeout(TIMEOUT)

# Enviar mensaje de descubrimiento
s.sendto(b"BUSCANDO HOLA", (broadcast_ip, port))
print(f"Enviado 'BUSCANDO HOLA' a {broadcast_ip}:{port}")

servidores = []
ip_primera_respuesta = None

# Esperar respuestas
start_time = time.time()
while True:
    try:
        data, addr = s.recvfrom(BUFFER_SIZE)
        mensaje = data.decode().strip()
        print(f"Respuesta de {addr[0]}: '{mensaje}'")
        if mensaje == "IMPLEMENTO HOLA":
            servidores.append(addr[0])
            if ip_primera_respuesta is None:
                ip_primera_respuesta = addr[0]
    except socket.timeout:
        break

# Mostrar servidores encontrados
print("\nServidores encontrados:")
for ip in servidores:
    print(f" - {ip}")

# Probar servicio HOLA con el primero
if ip_primera_respuesta:
    s.sendto(b"HOLA", (ip_primera_respuesta, port))
    try:
        respuesta, _ = s.recvfrom(BUFFER_SIZE)
        print(f"\nRespuesta del servidor {ip_primera_respuesta}: {respuesta.decode().strip()}")
    except socket.timeout:
        print("No se recibió respuesta al mensaje 'HOLA'")
else:
    print("No se encontraron servidores.")