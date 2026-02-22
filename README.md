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