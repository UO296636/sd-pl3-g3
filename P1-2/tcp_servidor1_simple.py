import socket
import sys

puerto = int(sys.argv[1]) if len(sys.argv) >= 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", puerto))

s.listen(5)  

print(f"Servidor escuchando en el puerto {puerto}...")

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)
    continuar = True
    while continuar:
        datos = sd.recv(5) 
        datos = datos.decode("ascii")  
        if datos == "":  
            print("Conexión cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False
        elif datos == "FINAL":
            print("Recibido mensaje de finalización")
            sd.close()
            continuar = False
        else:
            print("Recibido mensaje: %s" % datos)
