# Crear bots de Rasa y generar archivos de entrenamiento para ellos de forma automática, a partir de datos proporcionados con los que se construye el conocimiento


---

**Ejecutar programa (Ver primero INSTALL.md como guía de instalación) o puede Montarlo en Google Colab (RECOMENDADO) paso a paso, la guía está en la carpeta `Montar proyecto en Google Colab`**

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

