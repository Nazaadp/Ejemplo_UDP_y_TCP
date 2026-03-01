from socket import *

puerto_servidor = 5000

# 1. Creamos el socket. SOCK_STREAM indica que usaremos TCP.
socket_servidor = socket(AF_INET, SOCK_STREAM)
socket_servidor.bind(('', puerto_servidor))

# 2. El servidor entra en modo escucha (diferencia clave con UDP)
# El parámetro "1" es el tamaño de la cola de conexiones en espera
socket_servidor.listen(1)

print("El servidor TCP está listo para recibir conexiones...")

while True:
    # 3. accept() bloquea la ejecución hasta que llega un cliente
    # Crea un NUEVO socket dedicado exclusivamente a ese cliente
    socket_conexion, direccion = socket_servidor.accept()
    
    # 4. Usamos recv() y send() simples porque la conexión ya está establecida
    oracion = socket_conexion.recv(1024).decode()


    print(f'Recibido {oracion}  de cliente, respondiendo...')

    respuesta = "¡Hola! Conexión TCP establecida y mensaje procesado exitosamente."
    
    socket_conexion.send(respuesta.encode())
    
    # 5. Cerramos ESTA conexión específica, pero el servidor sigue escuchando
    socket_conexion.close()