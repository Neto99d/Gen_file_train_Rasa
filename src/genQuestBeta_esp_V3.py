import spacy
from collections import OrderedDict
import sys
import os
import cargaDatos
from datetime import datetime
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer, util
from transformers import T5ForConditionalGeneration, T5Tokenizer, BertTokenizer, BertModel, AutoTokenizer, AutoModelForSeq2SeqLM
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import torch
from transformers import BertTokenizer, BertModel, pipeline
from warnings import filterwarnings as filt

client = MongoClient()

# ............DEVUELVE PREGUNTAS mediante modelo entrenado y DEVUELVE LAS RESPUESTAS POR MODELO entrenado.......

OUTPUT_DIRECTORY = "output"
db = client['rasa_File_DB']
collection = db['temas']
collection_accion = db['acciones']

# modelo de spacy
nlp = spacy.load("es_core_news_lg")

# modelo Generador de respuestas
qa_pipeline = pipeline(
        "question-answering",
        model="mrm8488/electricidad-small-finetuned-squadv1-es",
        tokenizer="mrm8488/electricidad-small-finetuned-squadv1-es"
    )
# Otro modelo (mas pesado, 400 y pico MB en comparacion con los 98 MB del que esta puesto)
# IIC/roberta-base-spanish-sqac


# modelo Generador de preguntas (900 y pico MB)
mdl = AutoModelForSeq2SeqLM.from_pretrained(
            'mrm8488/bert2bert-spanish-question-generation')
tknizer = AutoTokenizer.from_pretrained(
            'mrm8488/bert2bert-spanish-question-generation')

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
        main(user)

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
        sentence = sent
        

        text = "context: {}".format(sentence)
        max_len = 256
        encoding = tknizer.encode_plus(
            text, max_length=max_len, pad_to_max_length=False, truncation=True, return_tensors="pt")

        input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

        outs = mdl.generate(input_ids=input_ids,
                            attention_mask=attention_mask,
                            early_stopping=True,
                            num_beams=5,
                            num_return_sequences=1,
                            no_repeat_ngram_size=2,
                            max_length=300)

        dec = [tknizer.decode(ids, skip_special_tokens=True)
               for ids in outs]

        Question = dec[0].replace("question:", "")
        Question = Question.strip()
       # print(Question)
       # Modelo genera respuestas y guarda en una lista
        '''result = qa_pipeline({
                    'context': str(sent),
                    'question': Question})'''
        questionsResult.append(Question)
        #answersResult.append(result['answer']) # Guarda respuestas en una lista
        
        # Oraciones como respuesta y Guarda en una lista
        answersResult.append(str(sent))
        
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
