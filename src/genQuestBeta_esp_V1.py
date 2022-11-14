import spacy
from collections import OrderedDict
import sys
import os
import cargaDatos
from datetime import datetime
from pymongo import MongoClient
from transformers import pipeline


client = MongoClient()

# ...............DEVUELVE PREGUNTAS por Spacy Entidades y DEVUELVE LAS ORACIONES COMO RESPUESTA.......


OUTPUT_DIRECTORY = "output"
db = client['rasa_File_DB']
collection = db['temas']
collection_accion = db['acciones']

# modelo de spacy
nlp = spacy.load("es_core_news_md")

# modelo Generador de respuestas
qa_pipeline = pipeline(
        "question-answering",
        model="mrm8488/electricidad-small-finetuned-squadv1-es",
        tokenizer="mrm8488/electricidad-small-finetuned-squadv1-es"
    )
# Otro modelo (mas pesado, 400 y pico MB en comparacion con los 98 MB del que esta puesto)
# IIC/roberta-base-spanish-sqac


def inicio(user):
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
            print()
            print(
                "Opción no disponible en estos momentos, por lo que se elegirá la numero 2 automáticamente")
            genQuest(asunto, user)
           # cargatextoDirecto(asunto, user)
        else:
            os.system("cls")
            genQuest(asunto, user)
    else:
        os.system("cls")
        print("<<<<<<< Este asunto ya existe, proporcione otro diferente. >>>>>>>>")
        print()
        inicio(user)

####################################################################################


def opcion(user):
    print()
    confirmar = input(
        "Desea cargar otro Contenido: Escriba si o no: ")
    if (confirmar == 'si'):
        os.system("cls")
        inicio(user)
    else:
        print()
        os.system("cls")
        cargaDatos.cargaDatos(user)


def genQuest(asunto, user):

    try:
        print()
        print("Entre la direccion del archivo de texto (archivo.txt) con el contenido")
        dirname, filename = os.path.split(os.path.abspath(__file__))
        # filename = "file.txt"
        # if os.path.exists(dirname+ os.path.sep + OUTPUT_DIRECTORY) == False:
        # os.makedirs(dirname+ os.path.sep + OUTPUT_DIRECTORY)

        # manual input() o directo open(directo dirname + os.path.sep + "file.txt",'r', encoding="utf-8")
        filehandle = open(input(), encoding="utf-8")
        textinput = filehandle.read()

       # ...........................................................................................
    except Exception as error:
        print()
        print()
        print("Error inesperado: ", error)
        print("Intente nuevamente")

    doc = nlp(textinput)
    # Lista de oraciones del texto

    # print(str(sentences))
    # arreglo para guardar las preguntas
    questions = []
    questionsResult = []
    answersResult = []
    sentences = list(doc.sents)
    for sent in sentences:
        docSent = nlp(str(sent))
        formaverbal = ""
        formaVerbalAUX = ""
        verbo = ""
        organizacion = ""
        personaje = ""

        # Extrayendo verbos, formas verbales al tokenizar la oracion
        for tok in docSent:
            # print(tok.text, tok.tag_, tok.dep_, tok.pos_)
            if(tok.tag_ == "VERB" and tok.dep_ == "ROOT"):
                formaverbal = tok.text
            elif(tok.tag_ == "AUX"):
                formaVerbalAUX = tok.text
            elif(tok.tag_ == "VERB" and tok.dep_ == "acl" or tok.dep_ == "advcl" or tok.dep_ == "relcl"):
                verbo = tok.text
        # print("FV: " + formaverbal, "FVAUX: " + formaVerbalAUX, "VERBO: " + verbo)
        # print("FIN DE TOKENIZACION")
        print()

        # Extrayendo entidades nombradas de la oracion
        for ent in docSent.ents:
            # print(ent.text, ent.start_char, ent.end_char, ent.label_)

            # Creando la pregunta de acuerdo al tipo de entidad y guardando las preguntas en un arreglo
            if(ent.label_ == "MISC"):
                if not ent.text in ["Twitter", "Facebook", "Instagram", "Linkedin", "Youtube", "Telegram"]:
                    questions.append('Que es {}'.format(ent.text))
            elif(ent.label_ == "PER"):
                personaje = ent.text
                questions.append('Quien es {}'.format(ent.text))
            elif(ent.label_ == "ORG"):
                organizacion = ent.text
                questions.append('Que paso en o con {}'.format(ent.text))
                questions.append('Quienes integran {}'.format(ent.text))
                if(formaverbal != "" and organizacion != "" and personaje != ""):
                    # pasando la forma verbal que puede verse como la accion que se ejecuto en la organizacion
                    questions.append('Quien {}'.format(
                        formaverbal) + " en {}".format(organizacion))
                # questions.append('A quien {}'.format(formaverbal))
            # Si se habla en la misma oracion sobre una persona y una organizacion
            '''if(organizacion != "" and personaje != ""):
                questions.append('Que significa o representa {} para {}'.format(
                    personaje, organizacion))'''
            if(ent.label_ == "LOC"):
                # questions.append('Que paso en {}'.format(ent.text))
                #questions.append('Que es o representa {}'.format(ent.text))
                questions.append(
                    'Donde queda o se sitúa {}'.format(ent.text))
            print()
        # print("FIN DE ENTIDADES")
        print()

        # eliminar duplicados
    OrderedDict.fromkeys(questions)  # Recordar orden de insercion
    set(questions)  # Eliminar duplicados

    # Lista de preguntas en orden sin duplicados
    questionsFIX = list(OrderedDict.fromkeys(questions).keys())
    # print("PREGUNTAS")
    # Mostrar preguntas
    # print(questionsFIX)

    print()
    print()
    print()
    # print("ANALIZANDO similitud de las preguntas con las oraciones")
    for pregunta in questionsFIX:
        docPregunta = nlp(str(pregunta))
        docPreguntaLimpio = nlp(
            ' '.join([str(t) for t in docPregunta if not t.is_stop]))  # sustantivos, verbos, palabras raiz o base
        for oracion in sentences:
            docOracion = nlp(str(oracion))
        # ' '.join([str(t) for t in main_doc if not t.is_stop])
        # ' '.join([str(t) for t in docOracion if t.pos_ in ['NOUN', 'PROPN']])
        # ' '.join([str(t) for t in docPregunta if t.pos_ in ['PROPN']]) + ''.join([str(t) for t in docPregunta if t.dep_ in ['ROOT', "acl", "advcl", "relcl"]]) + ''.join([str(t) for t in docPregunta if t.tag_ in ['VERB', "AUX"]])
            docOracionLimpio = nlp(
                ' '.join([str(t) for t in docOracion if not t.is_stop]))
            print("   =>Pregunta: " + str(pregunta) + "    " + "\n"
                  " Similitud pregunta-oracion: " + str(docPreguntaLimpio.similarity(docOracionLimpio)) + "   \n    " + "\n" + "Texto de oracion: " + str(oracion) + "\n")
            if( docPreguntaLimpio.similarity(docOracionLimpio) > 0.50):
                
                # OJOOOOOO SE REPITEN PREGUNTAS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                
                # questionsResult.append(pregunta)
                # answersResult.append(str(oracion)) 
                result = qa_pipeline({
                    'context': str(oracion),
                    'question': pregunta})
                questionsResult.append(pregunta)
                answersResult.append(result['answer'])

    # Mostrando resultado final
    os.system("cls")
    print()
    print('\n-----------ENTRADA de TEXTO-------------\n')
    print(textinput, '\n')
    print('\n-----------FIN de TEXTO---------------\n')
    print("Preguntas: \n" + str(questionsResult) + "\n" +
          "\n" + "Respuestas: \n" + str(answersResult) + "\n")
    # ......................................................................................

    # Trabajando en Base de datos
    # Insertando temas
    post = {"asunto": asunto,
            "user": user,
            "texto": textinput,
            "questions": questionsResult,
            "responses": answersResult,
            }
    post_id = collection.insert_one(post).inserted_id
    print()
    print("Operación finalizada con éxito, información guardada en su Base de Datos" + "\n")

    # Actualizando acciones
    collection_accion.update_one(
        {'userID': user}, {
            '$push': {"generaste_temas": {"asunto_tema": asunto, "temaID": post_id, "fecha_creado": datetime.today().strftime('%Y-%m-%d %I:%M %p')}}}
    )
    opcion(user)
