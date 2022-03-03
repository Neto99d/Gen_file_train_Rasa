from textblob import TextBlob
from collections import OrderedDict
import fileNLU
import fileDomain
import fileStories
import fileRules
import createAVirtual
import sys
import os
from deep_translator import GoogleTranslator
from pymongo import MongoClient

client = MongoClient()

OUTPUT_DIRECTORY = "output"


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
                   line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + '?'

    elif all(key in bucket for key in l9):  # 'NNP', 'VBZ', 'NN' in sentence
        question = 'What' + ' ' + \
                   line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + '?'

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
                   line.words[bucket['VBZ']] + ' ' + line.words[bucket['NN']] + '?'

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


def main():
    """
    Accepts a text file as an argument and generates questions from it.
    """
    global fix_questions  # lista donde se Limpiara preguntas duplicadas
    fix_questions = []
    global questionsEs
    questionsEs = []
    global responsesEs
    responsesEs = []
    global domainRasa
    domainRasa = fileDomain
    global nluRasa
    nluRasa = fileNLU
    global storiesRasa
    storiesRasa = fileStories
    global rulesRasa
    rulesRasa = fileRules
    # verbose mode is activated when we give -v as argument.
    global verbose
    verbose = False

    # Set verbose if -v option is given as argument.
    if len(sys.argv) >= 3:
        if sys.argv[2] == '-v':
            print('Verbose Mode Activated\n')
            verbose = True

    # Open the file given as argument in read-only mode.

    print("Ponga brevemente (es como un Título) de que trata su contenido: ")
    asunto = input()
    print("Asunto: " + asunto)
    print("Entre la direccion del archivo de texto con el contenido")  # AGREGADO
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

    parse(textinput)

    # TRADUCTOR
    for w in questions:
        traductor = GoogleTranslator(source='auto', target='es')
        resultado = traductor.translate(w)
        questionsEs.append(resultado)
    print(questionsEs)

    for w in responses:
        traductor = GoogleTranslator(source='auto', target='es')
        resultado = traductor.translate(w)
        responsesEs.append(resultado)
    print(responsesEs)
    ###########################

    # Trabajando en Base de datos

    db = client['rasa_File_DB']
    collection = db['contenido']
    post = {"asunto": asunto,
            "texto": textinput,
            "questions": questions,
            "responses": responses,
            }
    posts = db.collection
    post_id = collection.insert_one(post).inserted_id

    ############################

    if (domainRasa.domYaml(questionsEs, responsesEs) &
            nluRasa.nluYaml(questionsEs, responsesEs) &
            storiesRasa.storiesYaml(questionsEs, responsesEs) &
            rulesRasa.rulesYaml(questionsEs, responsesEs)):
        print(
            '\n' + "Creados con Exito :), en la carpeta Archivos_generados" + '\n' '..............................')
        print()
        createAVirtual.creaAsistente()
    else:
        print()
        print("Algo salio mal :( ")


if __name__ == "__main__":
    main()
