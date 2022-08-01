# Automáticamente :: Crear bots de Rasa y generar archivos de entrenamiento para ellos, a partir de datos proporcionados con los que se construye el conocimiento

**Instalar dependencias de la herramienta vía línea de comandos (cmd)**

- `pip install -r requirements.txt` para instalar todo de una vez

- O puede Instalar dependencias una a una ejecutando

     `pip install <package_name>`

  **nombres de paquetes**
  - rasa==3.0.0
  - nltk==3.4.5
  - textblob==0.15.0
  - ruamel.yaml==0.16.13
  - ruamel.yaml.clib==0.2.6
  - six==1.15.0
  - deep-translator==1.7.0
  - pymongo==3.10.1
  - spacy==3.1.0
  - en-core-web-md==3.1.0
  - es-core-news-md==3.1.0
  - bcrypt==3.2.2

---

**Código Personal**

- systemSGCA.py
- fileDomain.py  
- fileNLU.py
- fileRules.py
- fileStories.py  
- createAVirtual.py
- entrenarAsistente.py
- ConnectToTelegramBot.py
- ConfigToSpacyNLP_ES.py

**- Instalar MongoDb para Base de Datos**

- Descarga MongoDB desde: <https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-5.0.9-signed.msi>
- Para administrar la base de datos el RoboMongo 3T: <https://studio3t.com/download-studio3t-free>

---

El algoritmo de generación de preguntas fue levemente modificado, el código original está más abajo (Automatic Question Generation)
---

**Ejecutar programa por vía CMD**

  Ejecutar el archivo

- python systemSGCA.py

  El sistema ejecutará por defecto el módulo (questES.py) para Asistente Virtual en Español. Requiere Internet.
  
---

**Funcionamiento**

- Deberá crear una cuenta con un nombre de usuario y contraseña para entrar al sistema.
- Luego podrá iniciar sesión con sus credenciales y usar el programa.
- Se le pedirá entrar la dirección del fichero de texto con el contenido (solo inglés de momento) y luego de entrar la dirección presionar ENTER.
- Cómo se ejecuta el módulo para asistente virtual en español (este usa un traductor por el momento) igualmente el contenido entrado debe ser en inglés, se trabaja para cambiar a español, pero de momento es en inglés.

  **Automaticamente el programa hace lo siguiente:**
  - Se extraen las preguntas y respuestas (questions, responses).
  - Las respuestas son las oraciones del texto, exactamente se crea un par pregunta _ respuesta.
  - Se le envía esa información extraída a los diferentes ficheros mencionados que tienen la lógica de contrucción del conocimiento, además de tener las funciones para la generación del archivo en el formato que el asistente virtual de Rasa  maneja.
  - Se crearán los archivos de entrenamiento en la carpeta `Archivos_generados`.
  - Luego se creará y entrenará el Asistente Virtual siguiendo los pasos que se le pondrán. En este proceso los archivos de  entrenamiento se moverán automáticamente de `Archivos_generados` a la carpeta elegida por usted, que es donde tiene el  asistente virtual. (Los archivos irán exactamente a los directorios correspondientes para el funcionamiento).  
  - Luego podrá establecer una conversación de prueba con el Asistente Virtual.

---
**Módulo de conexión con Telegram. Si tiene un bot de Telegram y desea conectar este a su Asistente Virtual y poder interactuar desde esa plataforma**

- Ejecute `ConnectToTelegramBot.py` y proporcione los datos que se le piden.
- Modo de ejecución vía CMD:
  - `python ConnectToTelegramBot.py`

---
---

También en la carpeta `output` puede ver ejemplos de cómo quedan los archivos de entrenamiento en el formato del asistente virtual de Rasa usando la  herramienta
---

---

También en la carpeta `Tesis\Capturas de pantalla` puede ver ejemplos de la herramienta funcionando o ver el video que está en la carpeta Tesis
---

---
**Probar entrenamiento del Asistente**

- **Ejecutar estos comandos vía cmd a la carpeta donde se creó el bot de Rasa**
  - Ejecutar comando `rasa visualize` para ver la gráfica de aprendizaje y verificar entrenamiento.
  - Ejecutar comando `rasa shell`  para conversar con el bot.
  - Ejecutar comando `rasa run`  para correr el servidor de Rasa y pueda conversar con el bot por los canales que lo tenga conectado, como por ejemplo Telegram en caso de que haya habilitado la conexión a esta plataforma con el módulo antes mencionado.

---
------
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
