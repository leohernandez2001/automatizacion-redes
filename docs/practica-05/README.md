##Práctica 05. *Mi primer scprit en Python para la automatización de redes*
---
* *1. Objetivo*

Desarrollar y ejecutar un script en Python que permita configurar un router Cisco IOSv mediante una conexión Telnet, utilizando una topología de red simulada en GNS3.

---
* *2. Relación con las prácticas anteriores*

En las prácticas anteriores se preparó el entorno de trabajo, se construyó una topología de red en GNS3, se representó información de dispositivos mediante Python y se investigaron herramientas y recursos relacionados con la automatización de redes.

En esta práctica se continúa con ese trabajo, dando un paso más: ahora python no solamente representa información, sino que también permite enviar comandos para configurar directamente un dispositivo de red.

---
* *3. Topología y direccionamiento*
  
 Para realizar la práctica se utilizó lo siguiente:
  
| Dispositivo | Función | Dirección IP |
|---|---|---|
| Network Automation Container (NAC) | Ejecuta el script de Python y establece la conexión Telnet. | `192.168.42.235` |
| Ethernet switch | Permite la conexión entre los dispositivos de la topología. | No aplica |
| NAT Cloud | Proporciona conexión hacia la red externa. | No aplica |
| Switch Cisco IOSvL2 | Simula un switch de red. | No aplica |
| Router R1 | Recibe y ejecuta los comandos enviados por el script de Python. | `192.168.42.70` |
| Loopback 0 (R1) | Interfaz lógica configurada en el router. | `1.1.1.1/32` |
| Loopback 1 (R1) | Interfaz lógica configurada en el router. | `2.2.2.2/32` |

---

* *4. Versión de Python*

La versión de Python utilizada en el Network Automation Container (NAC) fue Python 3.8.5.

---

* *5. Problemas encontrados y soluciones*

  * Comando ipconfig no reconocido: se utilizó ifconfig para consultar la dirección IP del NAC.
  * Problemas iniciales de conectividad: al principio no se obtenía respuesta del router. Se revisó la configuración de red hasta conseguir comunicación entre ambos dispositivos.
  * Error al asignar la direccion IP: se presentó un error por escribir incompleta la máscara de subred. Se corrigió al faltar un 255 en la máscara.

---

* *6. Evidencias*

Las capturas de pantalla del procedimento se encuentran en la carpeta evidencias.

---

* *7. Conclusiones*

**Laura Valeria de la Luz Hernández** Durante esta actividad comenzamos preparando el programa GNS3 y creando nuestro espacio de trabajo. Después agregamos los dispositivos necesarios y realizamos las conexiones entre ellos. Aprendí cómo se comunican los equipos dentro de una red y cómo podemos utilizar herramientas para facilitar su configuración. También conocí cómo Python puede ayudarnos a realizar algunas tareas automáticamente, sin tener que escribir todos los comandos manualmente. 

**Leonel de la Luz Hernández** En esta práctica trabajamos con diferentes dispositivos dentro de GNS3 y aprendimos a conectarlos entre sí. Una de las partes principales fue lograr que el contenedor pudiera comunicarse con el router. Después utilizamos un pequeño programa en Python para enviar instrucciones y realizar cambios en el router. Con esto comprendí mejor cómo se pueden simplificar algunas tareas que normalmente se hacen de forma manual. 

**Marco Salazar Sánchez** Durante la actividad primero preparamos el entorno de trabajo y agregamos los dispositivos necesarios para crear nuestra red. Después configuramos el router para poder acceder a él desde el contenedor. Lo que más trabajamos fue el uso de Python para ejecutar instrucciones automáticamente, como crear nuevas interfaces y realizar otras configuraciones. Esta práctica me ayudó a entender mejor cómo se puede utilizar la programación para facilitar el trabajo en redes. 

**Mónica Vianey Valle Lucio** En esta actividad aprendimos a preparar una red utilizando GNS3 y a conectar diferentes dispositivos. También configuramos el router para poder acceder a él desde otro equipo y posteriormente realizamos algunas modificaciones utilizando un programa de Python. Durante el proceso comprobamos que los cambios se realizaran correctamente. En general, fue una práctica que nos ayudó a conocer nuevas herramientas y entender cómo podemos ahorrar tiempo al realizar configuraciones. 
