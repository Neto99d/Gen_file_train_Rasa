from textblob import TextBlob
from collections import OrderedDict
import sys
import os
import cargaDatos
from datetime import datetime
from deep_translator import GoogleTranslator
from pymongo import MongoClient

client = MongoClient()

OUTPUT_DIRECTORY = "output"
db = client['rasa_File_DB']
collection = db['temas']
collection_accion = db['acciones']


def parse(string):
    """
    Parse a paragraph. Devide it into sentences and try to generate quesstions from each sentences.
    """

    try:
        global responses  # Respuestas que se enviaran para archivos de Rasa
        responses = []

        txt = TextBlob(string)

        # Each sentence is taken from the string input and passed to genQuestion() to generate questions.
        for sentence in txt.sentences:
            genQuestion(sentence)
            # Pasando las oraciones del texto como respuestas para archivos Rasa
            responses.append(str(sentence))
        # print(responses)
    except Exception as e:
        raise e


def genQuestion(line):
    """
    outputs question from the given text
    """

    if type(line) is str:  # If the passed variable is of type string.
        line = TextBlob(line)  # Create object of type textblob.blob.TextBlob

    bucket = {}  # Create an empty dictionary

    for i, j in enumerate(line.tags):  # line.tags are the parts-of-speach in English
        if j[1] not in bucket:
            # Add all tags to the dictionary or bucket variable
            bucket[j[1]] = i

    if verbose:  # In verbose more print the key,values of dictionary
        print('\n', '-' * 20)
        print(line, '\n')
        print("TAGS:", line.tags, '\n')
        print(bucket)

    question = ''  # Create an empty string

    # These are the english part-of-speach tags used in this demo program.
    # .....................................................................
    # NNS     Noun, plural
    # JJ  Adjective
    # NNP     Proper noun, singular
    # VBG     Verb, gerund or present participle
    # VBN     Verb, past participle
    # VBZ     Verb, 3rd person singular present
    # VBD     Verb, past tense
    # IN      Preposition or subordinating conjunction
    # PRP     Personal pronoun
    # NN  Noun, singular or mass
    # .....................................................................

    # Create a list of tag-combination

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

    # With the use of conditional statements the dictionary is compared with the list created above

    # 'NNP', 'VBG', 'VBZ', 'IN' in sentence.
    if all(key in bucket for key in l1):
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
            bucket['VBG']] + '?'

    elif all(key in bucket for key in l2):  # 'NNP', 'VBG', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + ' ' + line.words[
            bucket['VBG']] + '?'

    # 'PRP', 'VBG', 'VBZ', 'IN' in sentence.
    elif all(key in bucket for key in l3):
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['PRP']] + ' ' + line.words[
            bucket['VBG']] + '?'

    elif all(key in bucket for key in l4):  # 'PRP', 'VBG', 'VBZ' in sentence.
        question = 'What ' + line.words[bucket['PRP']] + ' ' + ' does ' + line.words[bucket['VBG']] + ' ' + line.words[
            bucket['VBG']] + '?'

    elif all(key in bucket for key in l7):  # 'NN', 'VBG', 'VBZ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NN']] + ' ' + line.words[
            bucket['VBG']] + '?'

    elif all(key in bucket for key in l8):  # 'NNP', 'VBZ', 'JJ' in sentence.
        question = 'What' + ' ' + \
                   line.words[bucket['VBZ']] + ' ' + \
            line.words[bucket['NNP']] + '?'

    elif all(key in bucket for key in l9):  # 'NNP', 'VBZ', 'NN' in sentence
        question = 'What' + ' ' + \
                   line.words[bucket['VBZ']] + ' ' + \
            line.words[bucket['NNP']] + '?'

    elif all(key in bucket for key in l11):  # 'PRP', 'VBZ' in sentence.
        if line.words[bucket['PRP']] in ['she', 'he']:
            question = 'What' + ' does ' + line.words[bucket['PRP']].lower() + ' ' + line.words[
                bucket['VBZ']].singularize() + '?'

    elif all(key in bucket for key in l10):  # 'NNP', 'VBZ' in sentence.
        question = 'What' + ' does ' + \
                   line.words[bucket['NNP']] + ' ' + \
                   line.words[bucket['VBZ']].singularize() + '?'

    elif all(key in bucket for key in l13):  # 'NN', 'VBZ' in sentence.
        question = 'What' + ' ' + \
                   line.words[bucket['VBZ']] + ' ' + \
            line.words[bucket['NN']] + '?'

    # When the tags are generated 's is split to ' and s. To overcome this issue.
    if 'VBZ' in bucket and line.words[bucket['VBZ']] == "’":
        question = question.replace(" ’ ", "'s ")

    # Print the genetated questions as output.

    if question != '':
        print('\n', 'Question: ' + question)
        # lista que sera analizada para encontrar duplicados
        fix_questions.append(question)
        OrderedDict.fromkeys(fix_questions)  # Recordar orden de insercion
    set(fix_questions)  # Eliminar duplicados
    global questions
    # Lista de preguntas en orden sin duplicados
    questions = list(OrderedDict.fromkeys(fix_questions).keys())

############################################################
#######################################


def main(user):
    """
    Accepts a text file as an argument and generates questions from it.
    """
    ################################
    print()
    print("Ha entrado al Sistema de Generación de Conocimiento Automático para Asistentes Virtuales de RASA" + "\n")
    print("- Si desea cancelar cualquier operación y salir a la pantalla principal del Sistema presione Ctrl + C" + "\n" + "- Si le sale al presionar Ctrl +C: " +
          "¿Desea terminar el trabajo por lotes (S/N)?, " + "presione s para cerrar o n para iniciar nuevamente el sistema")
    print()
    ################################

    # verbose mode is activated when we give -v as argument.
    global verbose
    verbose = False

    # Set verbose if -v option is given as argument.
    if len(sys.argv) >= 3:
        if sys.argv[2] == '-v':
            print('Verbose Mode Activated\n')
            verbose = True

    # Open the file given as argument in read-only mode.

    print("Ponga brevemente un Asunto (es como un Título) de que trata el contenido que va a entrar, esto servirá para guardar e identificar los datos y ser usados nuevamente cuando desee: ")
    asunto = input()
    existe_asunto = collection.find_one({'asunto': asunto})
    if existe_asunto is None:
        print("Asunto: " + asunto)
        print()
        print("Proporcione un contenido (un texto o un archivo de texto) para extraer las posibles preguntas y respuestas" + "\n")
        print("OPCIONES" + "\n" "1. Cargar contenido con texto entrado directamente" +
              "\n" "2. Cargar contenido poniendo la direccion del archivo de texto (extensión .txt)")
        noOpcion = input(
            "Escriba el número de la opción: ")
        if (noOpcion == '1'):
            os.system("cls")
            cargaFicheroText(asunto, user)
           # cargatextoDirecto()
        else:
            os.system("cls")
            cargaFicheroText(asunto, user)
    else:
        os.system("cls")
        print("<<<<<<< Este asunto ya existe, proporcione otro diferente. >>>>>>>>")
        print()
        main(user)

####################################################################################


def opcion(user):
    print()
    confirmar = input(
        "Desea cargar otro Contenido: Escriba si o no: ")
    if (confirmar == 'si'):
        os.system("cls")
        main(user)
    else:
        print()
        os.system("cls")
        cargaDatos.cargaDatos(user)

#############################################################################


def cargatextoDirecto(asunto, user):
    try:
        print()
        print("Copie su texto y presione ENTER")
        textinput = input()

        # Send the content of text file as string to function parse()
        global fix_questions
        fix_questions = []

        parse(textinput)

        questionsEs = []
        responsesEs = []
        # TRADUCTOR ONLINE
        print()
        print("Traduciendo preguntas y respuestas................")
        print()
        for w in questions:
            traductor = GoogleTranslator(source='auto', target='es')
            resultado = traductor.translate(w)
            questionsEs.append(resultado)
        print("Preguntas: " + str(questionsEs))
        print()

        for w in responses:
            traductor = GoogleTranslator(source='auto', target='es')
            resultado = traductor.translate(w)
            responsesEs.append(resultado)
        print("Respuestas: " + str(responsesEs))
        ###########################

        # Trabajando en Base de datos
        # Insertando Temas
        post = {"asunto": asunto,
                "user": user,
                "texto": textinput,
                "questions": questionsEs,
                "responses": responsesEs,
                }
        post_id = collection.insert_one(post).inserted_id
        print()
        print("Operación finalizada con éxito, información guardada en su Base de Datos")
        
        # Actualizando acciones
        collection_accion.update_one(
            {'userID': user}, {
                '$push': {"generaste_temas": {"asunto_tema": asunto, "temaID": post_id, "fecha_creado": datetime.today().strftime('%Y-%m-%d %I:%M %p')}}}
        )

        opcion(user)
    except Exception as error:
        print(error)
        print("Error inesperado")
        print("Intente nuevamente")
######################################################################


def cargaFicheroText(asunto, user):
    try:
        print()
        print("Entre la direccion del archivo de texto (archivo.txt) con el contenido")
        dirname, filename = os.path.split(os.path.abspath(__file__))
        # filename = "file.txt"
        # if os.path.exists(dirname+ os.path.sep + OUTPUT_DIRECTORY) == False:
        # os.makedirs(dirname+ os.path.sep + OUTPUT_DIRECTORY)

        filehandle = open(dirname + os.path.sep + "file.txt",
                          'r')  # cambiado input()
        textinput = filehandle.read()
        print('\n-----------INPUT TEXT-------------\n')
        print(textinput, '\n')
        print('\n-----------INPUT END---------------\n')

        # Send the content of text file as string to function parse()
        global fix_questions
        fix_questions = []

        parse(textinput)

        questionsEs = []
        responsesEs = []

        # TRADUCTOR ONLINE
        print()
        print("Traduciendo preguntas y respuestas................")
        print()
        for w in questions:
            traductor = GoogleTranslator(source='auto', target='es')
            resultado = traductor.translate(w)
            questionsEs.append(resultado)
        print("Preguntas: " + str(questionsEs))
        print()

        for w in responses:
            traductor = GoogleTranslator(source='auto', target='es')
            resultado = traductor.translate(w)
            responsesEs.append(resultado)
        print("Respuestas: " + str(responsesEs))
        ###########################

        # Trabajando en Base de datos
        # Insertando temas
        post = {"asunto": asunto,
                "user": user,
                "texto": textinput,
                "questions": questionsEs,
                "responses": responsesEs,
                }
        post_id = collection.insert_one(post).inserted_id
        print()
        print("Operación finalizada con éxito, información guardada en su Base de Datos")

        # Actualizando acciones
        collection_accion.update_one(
            {'userID': user}, {
                '$push': {"generaste_temas": {"asunto_tema": asunto, "temaID": post_id, "fecha_creado": datetime.today().strftime('%Y-%m-%d %I:%M %p')}}}
        )
        opcion(user)
    except Exception as error:
        print(error)
        print("Error inesperado")
        print("Intente nuevamente")
