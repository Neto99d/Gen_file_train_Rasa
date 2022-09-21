# Crear bots de Rasa y generar archivos de entrenamiento para ellos de forma automática, a partir de datos proporcionados con los que se construye el conocimiento

**Código Personal**

- systemSGCA.py
- cargaDatos.py
- fileDomain.py  
- fileNLU.py
- fileRules.py
- fileStories.py  
- createAVirtualES.py
- IniciaWebChat.py
- generarArchivosEntrenamiento.py
- correrServerAsistente.py
- entrenarAsistenteES.py
- ConnectToTelegramBot.py

*El algoritmo de generación de preguntas (`Archivo questES.py`) fue hasta cierto punto modificado, el código original está más abajo (Automatic Question Generation)*
---

**Ejecutar programa (Ver primero INSTALL.md como guía de instalación)**

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

  **El programa hace lo siguiente en cada número de opción:**

  1. Es dónde se crea el Asistente Virtual `(deberá proporcionar un nombre y una descripción para el mismo)`, después de crear uno puede elegir si crear otro o no.

https://user-images.githubusercontent.com/68437647/190913895-a6f56fc5-d3c2-4654-9b17-1650ee56ce62.mp4


  2. Es dónde se generan datos de entrenamiento o el conocimiento en sí, y se hace primeramente el análisis del contenido (un texto o un archivo de texto con infomracón) que se le pedirá. Se extraen las preguntas y las respuestas (el contenido entrado por el momento debe ser en inglés, se busca una solución para idioma español), estas preguntas y respuestas serán traducidas en línea (online) al español y guardadas en una base de datos automáticamente las cuáles se usarán para los archivos de entrenamiento. Al finalizar tendrá la posibilidad de elegir cargar otro contenido o no. Tiene la ventaja de generar datos de entrenamiento y guardarlos sin tener aún asistentes creados, los cuales podrá entrenar luego con los datos que ha generado.
  

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
**Módulo de conexión con Telegram. Si tiene un bot de Telegram y desea conectar este a su Asistente Virtual y poder interactuar desde esa plataforma (Usuario Avanzado)**

- Ejecute `Conectar con su Telegram-Bot.bat` y proporcione los datos que se le piden.


------
------
---

# Funcionamiento de Generador de preguntas (Codigo Original de terceros)

# Automatic Question Generation

This program takes a text file as an input and generates questions by analyzing each sentence.
Also, create a RASA Virtual Assistan Configuration file copied in /output directory
with domain.yml name.

Note: A similar implementatin is [here](https://github.com/Neto99d/Gen_file_train_Rasa).

## Usage

**Virtualenv recommended**

`pip install -r requirements.txt`

`python -m textblob.download_corpora`
`python3 quest.py file.txt`

*Use `-v` option to activate verbose*

`python3 quest.py file.txt -v`

*You can also try inputing any text file.*

## How does this work?

**A text file passed as argument to the program.**

The text file is read using a Python package called **`textblob`**.
Each paragraph is further broken down into sentences using the function **`parse(string):`**
And each sentence is passed as string to function **`genQuestion(line):`**

**These are the part-of-speech tags which is used in this demo.**

```
NNS  Noun, plural
JJ  Adjective 
NNP  Proper noun, singular 
VBG  Verb, gerund or present participle 
VBN  Verb, past participle 
VBZ  Verb, 3rd person singular present 
VBD  Verb, past tense 
IN   Preposition or subordinating conjunction 
PRP  Personal pronoun 
NN  Noun, singular or mass 
```

**Ref:** [Alphabetical list of part-of-speech tags used in the Penn Treebank Project](http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

**This program uses a small list of combinations.**

```
    l1 = ['NNP', 'VBG', 'VBZ', 'IN']
    l2 = ['NNP', 'VBG', 'VBZ']
    l3 = ['PRP', 'VBG', 'VBZ', 'IN']
    l4 = ['PRP', 'VBG', 'VBZ']
    l5 = ['PRP', 'VBG', 'VBD']
    l6 = ['NNP', 'VBG', 'VBD']
    l7 = ['NN', 'VBG', 'VBZ']
    l8 = ['NNP', 'VBZ', 'JJ']
    l9 = ['NNP', 'VBZ', 'NN']
    l10 = ['NNP', 'VBZ']
    l11 = ['PRP', 'VBZ']
    l12 = ['NNP', 'NN', 'IN']
    l13 = ['NN', 'VBZ']
```

Each sentence is parsed using English grammar rules with the use of condition statements.
A dictionary is created called **`bucket`** and the part-of-speech tags are added to it.

The sentence which gets parsed successfully generates a question sentence.
The generated question list is printed as output.

**This demo only uses the grammar to generate questions starting with 'what'.**

## Example

**Sentence:**

-----------INPUT TEXT-------------

```
Bansoori is an Indian classical instrument. Akhil plays Bansoori and Guitar. 
Puliyogare is a South Indian dish made of rice and tamarind. 
Priya writes poems. 

Osmosis is the movement of a solvent across a semipermeable membrane toward a higher concentration of solute. In biological systems, the solvent is typically water, but osmosis can occur in other liquids, supercritical liquids, and even gases.
When a cell is submerged in water, the water molecules pass through the cell membrane from an area of low solute concentration to high solute concentration. For example, if the cell is submerged in saltwater, water molecules move out of the cell. If a cell is submerged in freshwater, water molecules move into the cell.

Raja-Yoga is divided into eight steps, the first is Yama -- non - killing, truthfulness, non - stealing, continence, and non - receiving of any gifts.
Next is Niyama -- cleanliness, contentment, austerity, study, and self - surrender to God. 

-----------INPUT END---------------
```

**Generated questions.**

```
 Question: What is Bansoori?

 Question: What does Akhil play?

 Question: What is Puliyogare?

 Question: What does Priya write?

 Question: What is Osmosis?

 Question: What is solvent?

 Question: What is cell?

 Question: What is example?

 Question: What is cell?

 Question: What is Raja-Yoga?

 Question: What is Niyama?
```

**We can also activate the `verbose` mode by -v argument to further understand the question generation process.**

**Output:** with verbose option.

```
 Bansoori is an Indian classical instrument. 

TAGS: [('Bansoori', 'NNP'), ('is', 'VBZ'), ('an', 'DT'), ('Indian', 'JJ'), ('classical', 'JJ'), ('instrument', 'NN')] 

{'NN': 5, 'JJ': 3, 'VBZ': 1, 'DT': 2, 'NNP': 0}

 Question: What is Bansoori?

 --------------------
Akhil plays Bansoori and Guitar. 

TAGS: [('Akhil', 'NNP'), ('plays', 'VBZ'), ('Bansoori', 'NNP'), ('and', 'CC'), ('Guitar', 'NNP')] 

{'CC': 3, 'VBZ': 1, 'NNP': 0}

 Question: What does Akhil play?

 --------------------
Puliyogare is a South Indian dish made of rice and tamarind. 

TAGS: [('Puliyogare', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('South', 'JJ'), ('Indian', 'JJ'), ('dish', 'NN'), ('made', 'VBN'), ('of', 'IN'), ('rice', 'NN'), ('and', 'CC'), ('tamarind', 'NN')] 

{'JJ': 3, 'IN': 7, 'NNP': 0, 'DT': 2, 'NN': 5, 'CC': 9, 'VBZ': 1, 'VBN': 6}

 Question: What is Puliyogare?

 --------------------
Priya writes poems. 

TAGS: [('Priya', 'NNP'), ('writes', 'VBZ'), ('poems', 'NNS')] 

{'VBZ': 1, 'NNS': 2, 'NNP': 0}

 Question: What does Priya write?

 --------------------
Osmosis is the movement of a solvent across a semipermeable membrane toward a higher concentration of solute. 

TAGS: [('Osmosis', 'NN'), ('is', 'VBZ'), ('the', 'DT'), ('movement', 'NN'), ('of', 'IN'), ('a', 'DT'), ('solvent', 'JJ'), ('across', 'IN'), ('a', 'DT'), ('semipermeable', 'JJ'), ('membrane', 'NN'), ('toward', 'IN'), ('a', 'DT'), ('higher', 'JJR'), ('concentration', 'NN'), ('of', 'IN'), ('solute', 'NN')] 

{'JJ': 6, 'IN': 4, 'DT': 2, 'NN': 0, 'VBZ': 1, 'JJR': 13}

 Question: What is Osmosis?
```

## How to improve this program

- This program generates questions starting with 'What'. We can add rule for generating questions containing 'How', 'Where', 'When', 'Which' etc.

- We can use a dataset of text and questions along with machine learning to ask better questions.

- Further, we can add complex semantic rules for creating long and complex questions.

- We can use pre-tagged bag of words to improve part-of-speech tags.

## Reference

[Alphabetical list of part-of-speech tags used in the Penn Treebank Project](http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

[Automatic Factual Question Generation from Text](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.208.5602&rep=rep1&type=pdf)

[TextBlob: Simplified Text Processing](http://textblob.readthedocs.io/en/dev/index.html)

[Automatic Question Generation from Paragraph](http://www.ijaerd.com/papers/finished_papers/Automatic%20Question%20Generation%20from%20Paragraph-IJAERDV03I1213514.pdf)

[K2Q: Generating Natural Language Questions from Keywords with User Refinements](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37566.pdf)

[Infusing NLU into Automatic Question Generation](http://www.aclweb.org/anthology/W16-6609)

[Literature Review of Automatic Question Generation Systems](https://pdfs.semanticscholar.org/fee0/1067ea9ce9ac1d85d3fd84c3b7f363a3826b.pdf)

[Neural Question Generation from Text: A Preliminary Study](https://arxiv.org/pdf/1704.01792.pdf)

[Learning to Ask: Neural Question Generation for Reading Comprehension [Apr 2017] ](https://arxiv.org/pdf/1705.00106.pdf)

[SQuAD: The Stanford Question Answering Dataset](https://rajpurkar.github.io/SQuAD-explorer/)
