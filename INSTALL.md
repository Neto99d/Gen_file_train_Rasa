# Guía de Instalación

---

*Sólo para Sistema Operativo Windows 7,8,10,11 con arquitectura x64*

*Requiere python 3.8 (Recomendado) en adelante*

- Descarga python 3.8 aquí: <https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe>

---

**Instalar dependencias de la herramienta con un click**

Ejecutar (Requiere Internet) para instalar todos los paquetes de python requeridos.

- `Instalar requerimientos python.bat`

---
Paquetes de python que serán instalados

- rasa==3.2.8
- nltk==3.4.5
- textblob==0.15.0
- ruamel.yaml==0.16.13
- ruamel.yaml.clib==0.2.6
- six==1.15.0
- deep-translator==1.7.0
- pymongo==3.10.1
- bcrypt==3.2.2

---

**Instalar MongoDb para Base de Datos**

- Descarga MongoDB desde: <https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-5.0.9-signed.msi>
  - *Al instalar MongoDB solo siga los pasos de instalación sin cambiar nada*

- `(Opcional)` Para administrar la base de datos puede usar el RoboMongo 3T: <https://studio3t.com/download-studio3t-free>

---
**Instalar las dll de Microsoft Visual para el funcionamiento del paquete Tensorflow**
(Si no se instala puede dar error este paquete)

- Instalar el archivo vc_redist.x64.exe que esta dentro del comprimido de mismo nombre.

---

**Al tener todo listo Ejecutar el programa :)**

- *Ojo, ejecutar como Administrador*

  *Ejecutar el archivo (Requiere Internet) que está en la carpeta `src`. Ver `Readme.md` para entender funcionamiento.*

- systemSGCA.bat

**Para usuarios avanzados, uso del módulo de Telegram para conectar su Asistente a su bot de Telegram**

*Requisitos*

- Saber como crear bots de Telegram y tener un bot de Telegram por cada asistente virtual que haya creado con el sistema
- Saber trabajar con ngrok o similares (Servicios o webhook para escuchar peticiones web)

*Ejecute el archivo*

- Ejecute `Conectar con su Telegram-Bot.bat` y proporcione los datos que se le piden.
- Una vez configurado inicie el servidor de su Asistente Virtual y podrá interactuar desde Telegram con su asistente.
