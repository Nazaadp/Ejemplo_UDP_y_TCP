from socket import *

# 1. Definimos el puerto de la aplicación (Capa 4)
puerto_servidor = 4000

# 2. Creamos el Socket. 
# AF_INET indica IPv4. SOCK_DGRAM indica que usaremos UDP.
socket_servidor = socket(AF_INET, SOCK_DGRAM)

# 3. Asignamos explícitamente el puerto al socket (bind)
socket_servidor.bind(('', puerto_servidor))

print("El servidor UDP está listo para recibir mensajes...")

# 4. Ciclo infinito pasivo
while True:
    # recvfrom() recibe el mensaje Y la dirección del cliente simultáneamente
    mensaje, direccion_cliente = socket_servidor.recvfrom(2048)

    print(f'Recibido - {mensaje} - de cliente, respondiendo...')

    respuesta = "¡Hola! Esta es una respuesta rápida desde el Servidor UDP."
    
    # sendto() dispara el paquete de texto hardcodeado usando la dirección guardada
    socket_servidor.sendto(respuesta.encode(), direccion_cliente)