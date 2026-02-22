from socket import *

nombre_servidor = '127.0.0.1'
puerto_servidor = 12000

socket_cliente = socket(AF_INET, SOCK_STREAM)

# 1. Establecemos el "Handshake" de 3 vías ANTES de enviar datos
socket_cliente.connect((nombre_servidor, puerto_servidor))

oracion = input('Ingresa una frase: ')

# 2. Enviamos el flujo de datos. No necesitamos especificar la IP destino de nuevo.
socket_cliente.send(oracion.encode())

# 3. Recibimos la respuesta
respuesta_servidor = socket_cliente.recv(1024)
print('Del Servidor:', respuesta_servidor.decode())

socket_cliente.close()