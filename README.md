# Crear bots de Rasa y generar archivos de entrenamiento para ellos de forma automática, a partir de datos proporcionados con los que se construye el conocimiento

**Información de la Tesis**

- Título: Herramienta digital para la construcción de conocimiento automático para un Asistente Virtual.
- Autor: Jorge Ernesto Duvalón Hernández
- Fecha de defensa de la Tesis: 21 de noviembre de 2022
- Tutor: MSc. Dionis López Ramos

```
Resumen
La población requiere respuestas inmediatas y acciones en tiempo real de 
diferentes servicios institucionales (Ej.: Salud, Legalidad, Seguridad, entre otros).
En los momentos actuales de desarrollo tecnológico y científico, los canales 
tradicionales de gestión no pueden satisfacer la demanda pico de búsqueda de 
información por parte de la población. Para resolver esta necesidad han sido 
creados los asistentes virtuales (Agentes Conversacionales) o robots 
conversacionales. Los asistentes virtuales son programas que intenta imitar la 
conversación que puede proveer un ser humano, además de concebirse como 
herramientas digitales que permiten la interacción hombre máquina. Los mismos 
son ampliamente utilizados en el sector empresarial, salud y gobierno porque 
garantizan una atención al usuario las 24 horas. 
A pesar de los grandes beneficios que proporcionan los asistentes virtuales, la 
creación del conocimiento que usan para dar respuestas a las preguntas y la 
interacción con los usuarios es laboriosa y costosa. Esto es debido a la 
necesidad de reunir especialistas y aglutinar la información necesaria para estos 
asistentes virtuales, además de que este arduo proceso puede dificultar la 
creación de los asistentes virtuales. 
En esta investigación se propone el diseño e implementación de una herramienta 
para la creación, entrenamiento y despliegue de asistentes virtuales, reduciendo 
la necesidad de la interacción con especialistas. Para la creación de esta 
herramienta y el despliegue de los asistentes virtuales se emplea el lenguaje de 
programación Python y el marco de trabajo Rasa especializado en la creación 
de asistentes virtuales.
```
---
```
Abstract
Title: “Digital tool for automatic building of a Virtual Assistants knowledge”.
The population requires immediate responses and real-time actions from different 
institutional services (eg, Health, Legality, Security, among others). In the current 
moments of technological and scientific development, the traditional 
management channels cannot satisfy the peak demand and the search for 
information. To solve this need, virtual assistants (Conversational Agents) or 
conversational robots have been created. Virtual assistants are programs that try 
to imitate the conversation that a human being can provide, in addition to being 
conceived as digital tools that allow human-machine interaction. They are widely 
used in the business, health and government sectors because they guarantee 
24-hour customer service. 
Despite the great benefits virtual assistants provide, creating the knowledge they 
use to answer questions and interact with users is time-consuming and 
expensive. This is due to the need to gather specialists and bring together the 
necessary information for these virtual assistants, in addition to the fact that this 
arduous process can make it difficult to create virtual assistants. 
This research proposes the design and implementation of a tool for the creation, 
training and deployment of virtual assistants, reducing the need for interaction 
with specialists. For the creation of this tool and the deployment of virtual 
assistants, the Python programming language and the Rasa framework 
specialized in the creation of virtual assistants are used
```
---
```
Para instalar y desplegar la herramienta necesita instalar las dependencias (paquetes de Python), entre las dependencias más importantes: Rasa Framework para crear Asistentes Virtuales y Spacy para procesamiento del lenguaje natural. También requiere conexión a Internet ya que necesita descargar algunos datos para funcionar. Necesita instalar MongoDb para la base de datos de la aplicación.
```
---
**Para instalar la herramienta ver el archivo Install.md en la carpeta Install**
---
---
**Ejecución de la Aplicación Informática**

  Ojo, ejecutar como Administrador

  Ejecutar el archivo (Requiere Internet). Se aconseja que tenga internet para usar la herramienta.

- systemSGCA.bat

---

**Funcionamiento**

- Deberá crear una cuenta con un nombre de usuario y contraseña para entrar al sistema.
- Luego podrá iniciar sesión con sus credenciales y usar el programa.
- Actualización respecto al video de muestra: Ahora la contraseña al iniciar sesión no se ve al escribir.


https://user-images.githubusercontent.com/68437647/190913817-73b16916-c35a-474c-ab33-94da97b475af.mp4



El sistema le mostrará varias opciones:
   1. Crear Asistente Virtual
   2. Generar Conocimiento
   3. Entrenar Asistente
   4. Probar Asistente

 *En cada una de las opciones el sistema lo guiará paso a paso, y le dirá que tiene que hacer*
 - *En los videos salen 5 opciones, esta 5ta opción fue eliminada*
 - *Y en los videos se entran datos en ingles, esto ya no es necesario, no debe entrar datos en ese idioma*
 - *La primera vez que se corra la herramienta descargará archivos necesarios para funcionar*

  **El programa hace lo siguiente en cada número de opción:**

  1. Es dónde se crea el Asistente Virtual `(deberá proporcionar un nombre y una descripción para el mismo)`, después de crear uno puede elegir si crear otro o no.

https://user-images.githubusercontent.com/68437647/190913895-a6f56fc5-d3c2-4654-9b17-1650ee56ce62.mp4


  2. Es dónde se generan datos de entrenamiento o el conocimiento en sí, y se hace primeramente el análisis del contenido (un texto o un archivo de texto con infomracón) que se le pedirá. Se extraen las preguntas y las respuestas y guardadas en una base de datos automáticamente las cuáles se usarán para los archivos de entrenamiento. Al finalizar tendrá la posibilidad de elegir cargar otro contenido o no. Tiene la ventaja de generar datos de entrenamiento y guardarlos sin tener aún asistentes creados, los cuales podrá entrenar luego con los datos que ha generado.
  

https://user-images.githubusercontent.com/68437647/190913946-2de837d9-e1c4-4a8c-b278-94c5ad6b69b2.mp4


  3. Es dónde se realiza el proceso de entrenamiento del asistente virtual. Se cargan los datos que el usuario tenga guardados y podrá elegir que contenido cargará para generar los archivos de entrenamiento y configuración para el asistente (Se crearán los archivos de entrenamiento y configuración en la carpeta `Archivos_generados`), luego saldrá una lista de los asistentes virtuales que el usuario haya creado (Mostrará el nombre del asistente y si este ha sido entrenado o no) y elegirá que asistente quiere entrenar con dichos archivos los cuáles se moverán automáticamente una vez empiece el entrenamiento (verá la información completa de dicho asistente y confirmará que es ese el que desea cargar). También se mostrará después del entrenamiento en el navegador, un *gráfico con el conocimiento del Asistente donde podrá apreciar si las preguntas corresponden con las respuestas inferidas después del entrenamiento `(pregunta -> utter_pregunta (respuesta inferida))`*, y si es correcto el bot tendrá alta probabilidad de responder correctamente. (Puede ver el gráfico en cualquier momento si va a la carpeta correspondiente al asistente virtual que quiere y ejecutar el archivo `graph.html`).
  

https://user-images.githubusercontent.com/68437647/190913979-75e40c27-746a-48f3-aad7-bd296e9e1516.mp4


Vista del gráfico de conocimiento:
![Captura web_18-9-2022_11949_](https://user-images.githubusercontent.com/68437647/190914156-090a760f-c34c-4f0a-8c4c-85bd02e1ae0a.jpeg)

  4. Esta parte como bien dice es para probar el asistente, se mostrará una lista con los asistentes virtuales del usuario y podrá elegir cuál quiere probar, luego podrá establecer una conversación con el asistente elegido de esta forma:

- Priemero una vez elegida esta opción y el asistente a probar, espere a que el servidor corra; cuando vea el mensaje `root  - Rasa server is up and running.` es que ya esta corriendo.


https://user-images.githubusercontent.com/68437647/190913740-12aa170b-98dd-4ea9-9368-3b7a187f3f8a.mp4



- Luego al ver este mensaje puede ejecutar el archivo `IniciarWebChat.bat` que le abrirá automáticamente en su navegador un sitio web con un componente de Chat para conversar con su Asistente.

Vista del sitio web y la interacción con el Asistente Virtual:


https://user-images.githubusercontent.com/68437647/190913068-8f71a379-ff2a-40ef-bd78-5229d485dbeb.mp4

---
**Agregue el widget chat oficial de Rasa al código de su página web (requiere internet para funcionar)**
- En el atributo `data-websocket-url` recibe la dirección desde donde corre el servidor del asistente virtual, en este caso corre en modo local por el puerto 5005.

`<!-- Widget Rasa Bot-->
    <div class="position-relative" id="rasa-chat-widget" data-websocket-url="http://localhost:5005"></div>
    <!-- Bootstrap core JS-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Core theme JS-->
    <script src="js/scripts.js"></script>
    <!-- CIERRE Widget Rasa Bot-->`

---
**Módulo de conexión con Telegram. Si tiene un bot de Telegram y desea conectar este a su Asistente Virtual y poder interactuar desde esa plataforma (Usuario Avanzado)**

- Ejecute `Conectar con su Telegram-Bot.bat` y proporcione los datos que se le piden.

