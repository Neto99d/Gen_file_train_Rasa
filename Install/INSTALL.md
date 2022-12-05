# Guía de Instalación

---

*Sólo para Sistema Operativo Windows 7,8,10,11 con arquitectura x64*

*Requiere python 3.8 (Recomendado) en adelante*

- Descarga python 3.8 aquí: <https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe>

---
**Ramas del proyecto**
- main `Esta rama funciona con Modelos pre-entrenados para generar preguntas y respuestas en español` por lo que si se instala desde esta rama funcionará con dichos Modelos por defecto.
- develop_neto_ES_ModelsQA `Rama develop de la principal MAIN.
- develop_ES_Spacy_ModelSimilarity `Esta rama funciona con Modelos pre-entrenados para generar respuestas y otro para análisis de similitud entre textos u oraciones, y Spacy para generar preguntas mediante entidades nombradas en español`.
- develop_neto_EN_a_ES `Esta rama funciona con algoritmo de tercero que funciona con datos de entrada en inglés generando preguntas en dicho idioma. Se hace una traduccion al español de los datos y las preguntas`.

**Opcionalmente en la carpeta Tools/Montar proyecto en Google Colab se puede tomar el archivo que contiene y correrlo en Google Colab, este archivo es para probar el proyecto en dicha plataforma, permite instalar paso a paso**

**Instalar dependencias de la herramienta con un click**

Ejecutar (Requiere Internet) para instalar todos los paquetes de python requeridos.

- `Instalar requerimientos python.bat`

---
Paquetes de python que serán instalados

- rasa==3.2.8
- ruamel.yaml==0.16.13
- ruamel.yaml.clib==0.2.6
- six==1.15.0
- pymongo==3.10.1
- bcrypt==3.2.2
- spacy==3.4.0
- transformers
- sentence_transformers

Puede que si tiene problemas con el paquete tensorflow, tenga que actualizar el mismo a la versión 2.9, ejecute el archivo de la carpeta Install:
- Actualizar Tensorflow.bat
---
**Instalar las dll de Microsoft Visual para el funcionamiento del paquete Tensorflow**
(Si no se instala puede dar error este paquete)

- Instalar el archivo vc_redist.x64.exe que esta dentro del comprimido de mismo nombre que está en la carpeta Tools.
---

**Instalar MongoDb para Base de Datos**

- Descarga MongoDB desde: <https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-5.0.9-signed.msi>
  - *Al instalar MongoDB solo siga los pasos de instalación sin cambiar nada*

- `(Opcional)` Para administrar la base de datos puede usar el RoboMongo Studio 3T: Descargar ultima versión: <https://studio3t.com/download-studio3t-free> o instalar Robo3T versión antigua pero más simple de usar que está en la carpeta Tools.

---

**Al tener todo listo Ejecutar el programa :)**

- *Ojo, ejecutar como Administrador*

  *Ejecutar el archivo (Requiere Internet) que está en la carpeta `src`. Ver `Readme.md` para entender funcionamiento.*
  
  *La primera vez que se corra la herramienta descargará archivos necesarios para funcionar*

- systemSGCA.bat

**Para usuarios avanzados, uso del módulo de Telegram para conectar su Asistente a su bot de Telegram**

*Requisitos*

- Saber como crear bots de Telegram y tener un bot de Telegram por cada asistente virtual que haya creado con el sistema
- Saber trabajar con ngrok o similares (Servicios o webhook para escuchar peticiones web)

*Ejecute el archivo*

- Ejecute `Conectar con su Telegram-Bot.bat` y proporcione los datos que se le piden.
- Una vez configurado inicie el servidor de su Asistente Virtual y podrá interactuar desde Telegram con su asistente.
