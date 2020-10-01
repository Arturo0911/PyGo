# Todo sobre los protocolos que debemos saber.


## All commands needs sudo before. Commands to use nmap 
    - arp-scan -l => permite buscar todos los dispositivos que están conectados a la red
    - nmap -sS <ip> => permite revisar todos los puertos que se encuentran trabajando.
    - nmap -O <ip> => permite establecer información acerca del sistema operativo que está corriendo en el servidor o el target
    - nmap -sV <ip> => permite verificar el puerto que está abierto y encima verifica la versión que está corriendo en cada puerto (en uno de estos puertos, hay verias aplicaciones
        que pueden tomar control del tráfico)
    - nmap -sL <ip> => Sondeo de lista de descubrimiento de sistemas; no envía ningún paquete, solo listará cada equipo de las redes especificadas. este proceso realiza una resolución
        inversa DNS en los equipos para obtemer sus nombres
    - nmap -sP <ip> => Barrido de ping(Ping sweep) método para descubrir dispositivos en línea example: nmap -sP 192.168.0.*

## Scripting using nmap and bash

    - nmap -sS 192.168.100.1 | grep open | cat >> <cualquier nombre de archivo.txt> => imprimirá todas las líneas que hagan match con la expresión "open" y se 
        guardarán en el archivo que se creará usnado el bash "cat"




## PORTS AND PROTOCOLS

### TCP
    - TCP ( protocolo de control de transmisión ) => este protocolo nos permite que se puedan comunicar las aplicaciones
        independientemente de las capas inferiores; esto signigica que los routers (capa de red en el medio TCP/IP) tienen que enviar segmentos
        (unidad de medida de TCP) de que si van a llegar estos datos a su destino de manera correctamente o no.
    - TCP da multiples soportes a los protocolos de la capa de aplicación como por ejempolo:
        - HTTP(web) HTTPS (web segura) POP3 (correo entrante) y SMTP(correo saliente) así como sus versiones seguras
            usando TLS.
        - FTP
        - FTPES
        - SFTP (para transferir archivos de un origen a un destino)
    - El protocolo TCP se encarga de la transmisión de datos, si por algún motivo se perdiesen, corrompiesen; este empezaría la retransmisión de datos.
        sin que intervenga la capa de apliación. De esta manera se garantiza que los datos lleguen a su destino sin ningún problema. 
    

### UDP 

    - UDP (Protocolo de datagramas de usuario) Se encarga de que las aplicaciones puedan comunicarse sin ningún problema en la capa de aplicación
        enviando datagramas (unidad de medida del protocolo UDP); esto significa que los routers solo deben enviar los datagramas.


### PROTOCOLS

    - ACK => acknowledgement, es un mensaje que el destino de la comunicación envia al origen para confirmar la recepción de un mensaje; si el mensaje
        está protegido por un codigo detector de errores y el dispositivo de destino posee además capacidad para procesar dicha información, el ACK también
        puede informar si ha recibido de forma íntegra el mensaje, sin ningún cambio. 










# MODELO TCP/IP

![Greeting Started](./screenshots/tcp_ip.png)
