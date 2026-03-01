from socket import *

# 1. Definimos la IP destino (Capa 3) y el puerto (Capa 4)
nombre_servidor = '127.0.0.1' # Localhost para pruebas
puerto_servidor = 4000

# 2. Creamos el socket activo del cliente
socket_cliente = socket(AF_INET, SOCK_DGRAM)

mensaje = input('Ingresa una frase: ')

# 3. Disparamos el datagrama. No hay connect(). 
socket_cliente.sendto(mensaje.encode(), (nombre_servidor, puerto_servidor))

# 4. Esperamos la respuesta
respuesta_servidor, direccion_servidor = socket_cliente.recvfrom(2048)
print('Respuesta del servidor:', respuesta_servidor.decode())

# 5. Cerramos el socket
socket_cliente.close()