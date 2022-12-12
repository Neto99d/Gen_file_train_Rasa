**Pruebas realizadas en Jmeter 5.5**

Descarga Jmeter Aqui: https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.5.zip

**Jmeter**

- La aplicación Apache JMeter™ es un software de código abierto, una aplicación Java 100% pura diseñada para cargar el comportamiento funcional de la prueba y medir el rendimiento. Fue originalmente diseñado para probar aplicaciones web, pero tiene desde entonces expandido a otras funciones de prueba.

**Las características de Apache JMeter incluyen:**

- Capacidad para cargar y probar el rendimiento de muchos tipos diferentes de aplicaciones/servidores/protocolos:
- Web - HTTP, HTTPS (Java, NodeJS, PHP, ASP.NET, ...)
- Servicios web SOAP / REST
- FTP
- Base de datos a través de JDBC
- LDAP
- Middleware orientado a mensajes (MOM) a través de JMS
- Correo: SMTP(S), POP3(S) e IMAP(S)
- Comandos nativos o scripts de shell
- TCP
- Objetos Java

Más Info: https://jmeter.apache.org/index.html

---
---
- MI PC de Prueba: Intel Core i3 6100U 2.3 Gz (6ta Gen) 8GB RAM

- Peticiones simulando 50, 100 y 120 usuarios cada x tiempo en segundos va incrementando a estas cifras de usuarios aun cuando esta trabajando con el primer lote de usuarios.

- El archivo statistics.csv y summary.csv muestra tabla con datos de las pruebas en cifras

**Muestras: Número total de muestras**
Promedio: Tiempo promedio. (milisegundos, correr tres lugares la coma hacia la izquierda para convertir a segundos)
Min: Este es el tiempo mínimo que ha tardado un muestreador en ir al servidor.
Max : Esta es la solicitud de tiempo máximo que se tarda en ir al servidor.
Error%: Número de muestreador de errores / Número total de muestreador.
Rendimiento: El rendimiento es la muestra por segundo que recibe el servidor. 
KB recibidos / segundo: Esto define cuántos kilobytes por segundo recibe el Cliente.
KB enviados / segundo: Esto define cuántos kilobytes por segundo se envían al servidor.
90% Línea: Representa que el 10% de los muestreadores han superado el tiempo para llegar al servidor.
95% Línea: Representa que el 5% de los muestreadores han superado el tiempo para llegar al servidor.
99% Línea: Representa que el 1% de los muestreadores ha excedido el tiempo para llegar al servidor.
 

- EL grafico muestra la media de tiempo de respuesta, el pico en el 95% de prueba y el minimo de tiempo de respuesta alcanzado, todo esto para 50, 100 y 120 usuarios.