# 🌐 Capa de Transporte: Implementación de Sockets en Python

Este repositorio contiene la demostración práctica de la Unidad 3 (Capa de Transporte) para la materia Redes de Computadoras. Incluye la implementación de la API de Sockets en Python para los protocolos TCP (Transmisión confiable orientada a la conexión) y UDP (Transmisión rápida de datagramas).

## 📂 Estructura de Archivos

* `servidor_udp.py`: Escucha pasiva y respuesta de datagramas sin estado.
* `cliente_udp.py`: Envío activo de datagramas mediante `sendto()`.
* `servidor_tcp.py`: Escucha activa (`listen()`), aceptación de conexiones (`accept()`) y procesamiento de flujos.
* `cliente_tcp.py`: Establecimiento de conexión formal (`connect()`) antes de la transmisión.

## 🌍 Casos de Uso Real (Transferencia Contextual)

La elección entre estos scripts en un entorno de producción depende de los requerimientos críticos de la aplicación. A continuación, se detallan dos escenarios reales:

### Escenario 1: Transmisión de Video en Vivo (Streaming) => **Uso de UDP**
* **El Problema Inicial:** Al usar TCP para video en vivo, la pérdida de un solo paquete obliga al protocolo a pausar la reproducción para solicitar su retransmisión (conocido como *buffering*).
* **El Análisis:** El ojo humano tolera la pérdida de algunos cuadros de video, pero la experiencia del usuario se arruina con las interrupciones constantes.
* **La Solución (Scripts UDP):** Al implementar los sockets UDP, despachamos los cuadros de video a máxima velocidad. Si un paquete se pierde, simplemente se ignora y se muestra el siguiente cuadro, garantizando una fluidez constante en tiempo real.

### Escenario 2: Transferencia de Documentos Importantes => **Uso de TCP**
* **El Problema Inicial:** Al intentar enviar un archivo ZIP o un PDF mediante UDP, la falta de control de flujo y la entrega desordenada de datagramas resulta en un archivo final corrupto o ilegible.
* **El Análisis:** En la transferencia de archivos, la integridad absoluta de los datos es innegociable. No importa si tarda unos milisegundos más, cada byte debe llegar en el orden exacto.
* **La Solución (Scripts TCP):** Implementar la arquitectura TCP asegura que el sistema operativo gestione la confirmación de recepción (ACKs) y el reensamblaje ordenado. El archivo llega a su destino siendo una copia exacta del original.

## 🚀 Instrucciones de Ejecución

**Requisito previo:** Python 3.x instalado en el sistema.

### Ejecución UDP (Demostración de Rapidez)
1. Abre una terminal e inicia el servidor pasivo:
   ```bash
   python Servidor_UDP.py

2. Abre una segunda terminal e inicia el servidor pasivo:
   ```bash
   python Cliente_UDP.py

3. Ingresa una frase y observa la respuesta instantánea sin necesidad de un handshake previo.

### Ejecución TCP (Demostración de Conexión)
1. Abre una terminal e inicia el servidor:
   ```bash
   python Servidor_TCP.py

2. Abre una segunda terminal y conecta el cliente:
   ```bash
   python Cliente_TCP.py

3. Ingresa una frase. Nota cómo el servidor crea un nuevo socket dedicado internamente mediante accept() para procesar esta conexión de forma confiable.



## 1. El Ecosistema UDP: Comunicación Sin Conexión

En UDP, la comunicación se asemeja a un servicio postal. No hay garantía de entrega ni orden, pero la velocidad es máxima debido a la ausencia de un proceso de conexión inicial.

| Fase | Servidor UDP (`servidor_udp.py`) | Cliente UDP (`cliente_udp.py`) |
| :--- | :--- | :--- |
| **1. Inicialización** | `sock_serv = socket(AF_INET, SOCK_DGRAM)`<br>Crea un socket pasivo para datagramas. | `sock_cli = socket(AF_INET, SOCK_DGRAM)`<br>Crea un socket activo para datagramas. |
| **2. Asignación** | `sock_serv.bind(('', 12000))`**<br>**Se "ata" rígidamente al puerto 12000 para que los clientes sepan a dónde enviar. | *(Implícita)*<br>El sistema operativo le asigna un puerto efímero aleatorio al momento de enviar. |
| **3. ¿Qué espera?** | `mensaje, dir = sock_serv.recvfrom(2048)`<br>**Espera:** Un datagrama entrante. Se bloquea (o usa timeout) hasta que un paquete golpea el puerto 12000. | `mensaje = input("Ingrese frase:")`<br>**Espera:** Que el usuario humano escriba el mensaje por teclado. |
| **4. ¿Qué hace y cómo?** | **Hace:** Extrae los datos y guarda la IP/Puerto de origen (`dir`).<br>Luego, procesa el *print* de recepción. | **Hace:** Dispara el mensaje hacia la red.<br>`sock_cli.sendto(msj, (ip_serv, 12000))` |
| **5. Respuesta** | `sock_serv.sendto(respuesta, dir)`<br>**Hace:** Dispara la respuesta hardcodeada exactamente a la dirección que guardó en el paso 3. | `res, dir = sock_cli.recvfrom(2048)`<br>**Espera:** El datagrama de vuelta desde el servidor para imprimirlo en pantalla. |

---

## 2. El Ecosistema TCP: Comunicación Orientada a la Conexión

En TCP, la comunicación se asemeja a una llamada telefónica. Hay un protocolo estricto de saludo de 3 vías (*Three-way Handshake*) antes de que se envíe el primer byte de datos útiles.

| Fase | Servidor TCP (`servidor_tcp.py`) | Cliente TCP (`cliente_tcp.py`) |
| :--- | :--- | :--- |
| **1. Inicialización** | `sock_serv = socket(AF_INET, SOCK_STREAM)`<br>Crea un socket pasivo para flujos continuos. | `sock_cli = socket(AF_INET, SOCK_STREAM)`<br>Crea un socket activo para flujos continuos. |
| **2. Preparación** | `sock_serv.bind(('', 12000))` y luego `sock_serv.listen(1)`<br>Abre la puerta y configura una cola de espera para 1 cliente. | *(Ninguna acción pasiva previa)* |
| **3. Conexión (El Saludo)** | `sock_dedicado, dir = sock_serv.accept()`<br>**Espera:** Una petición de conexión.<br>**Hace:** Clona el socket original y crea uno **nuevo** (`sock_dedicado`) exclusivo para este cliente. | `sock_cli.connect((ip_serv, 12000))`<br>**Hace:** Inicia el saludo de 3 vías de forma invisible para el programador. |
| **4. Transferencia** | `datos = sock_dedicado.recv(1024)`<br>**Espera:** El flujo de bytes a través del canal ya establecido. | `sock_cli.send(mensaje.encode())`<br>**Hace:** Empuja los datos por el canal seguro. Ya no necesita indicar la IP de destino. |
| **5. Finalización** | `sock_dedicado.send(respuesta)`<br>`sock_dedicado.close()`<br>**Hace:** Responde y luego destruye el socket exclusivo. El socket principal sigue vivo en su ciclo. | `respuesta = sock_cli.recv(1024)`<br>`sock_cli.close()`<br>**Hace:** Recibe la respuesta, cierra su socket y termina la ejecución. |