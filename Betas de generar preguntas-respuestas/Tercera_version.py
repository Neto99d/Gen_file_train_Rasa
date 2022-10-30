import spacy
from spacy import displacy
from collections import OrderedDict
from transformers import pipeline
import numpy as np
from sentence_transformers import SentenceTransformer, util

nlp = spacy.load("es_core_news_lg")

# modelo Generador de respuestas
qa_pipeline = pipeline(
        "question-answering",
        model="mrm8488/electricidad-small-finetuned-squadv1-es",
        tokenizer="mrm8488/electricidad-small-finetuned-squadv1-es"
    )
# Otro modelo (mas pesado, 400 y pico MB en comparacion con los 98 MB del que esta puesto)
# IIC/roberta-base-spanish-sqac


texto = '''Código de las Familias es una norma sustantiva del Derecho de Familia en Cuba; Cuerpo legal que regula todas las instituciones relativas a la familia: el matrimonio, el divorcio, las relaciones paterno filiales, la obligación de dar alimentos, la adopción y la tutela. Se promulga en 1975, modificado y propuesto a referendo popular el 25 de septiembre de 2022, siendo ratificado por el pueblo cubano con el 66.87 % de los votos.
Las normas contenidas en este Código se aplican a todas las familias cualquiera que sea la forma de organización que adopten y a las relaciones jurídico-familiares que de ellas se deriven entre sus miembros, y de estos con la sociedad y el Estado y se rigen por los principios, valores y reglas contenidos en la Constitución de la República de Cuba, los tratados internacionales en vigor para el país que tienen incidencia en materia familiar y los previstos en este Código.
Es un Código inclusivo, revolucionario y novedoso en su texto como en su proceso de elaboración. Protege a niños, niñas y adolescentes, les reconoce derechos a las personas adultas mayores y en situación de discapacidad, visibiliza y reconoce derechos a sectores vulnerables, condena la violencia familiar y establece herramientas para los que han sido víctima de ella, condena la discriminación contra la mujer, democratiza las relaciones familiares, le otorga efectos jurídicos al afecto, y reconoce en su articulado la diversidad de realidades que existe entre las familias cubanas.'''

doc = nlp(texto)
sentences = list(doc.sents)
# print(sentences)


def gen():
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
        docPregunta = nlp(str(pregunta))  # paso la pregunta al documento Spacy

        # Vector (limpiando documento)
        docPreguntaLimpio = nlp(
            ' '.join([str(t) for t in docPregunta if not t.is_stop]))  # Vector sin stop_words

        for oracion in sentences:
            docOracion = nlp(str(oracion))

        # Vectores con sustantivos y pronombres solamente
        # ' '.join([str(t) for t in docOracion if t.pos_ in ['NOUN', 'PROPN']])

        # Vectores con varias caegorias gramaticales
        # ' '.join([str(t) for t in docPregunta if t.pos_ in ['PROPN']]) + ''.join([str(t) for t in docPregunta if t.dep_ in ['ROOT', "acl", "advcl", "relcl"]]) + ''.join([str(t) for t in docPregunta if t.tag_ in ['VERB', "AUX"]])

            docOracionLimpio = nlp(
                ' '.join([str(t) for t in docOracion if not t.is_stop]))

            # Mostrar traza de analisis
            print("   =>Pregunta: " + str(pregunta) + "    " + "\n"
                  " Similitud pregunta-oracion: " + str(docPreguntaLimpio.similarity(docOracionLimpio)) + "   \n    " + "\n" + "Texto de oracion: " + str(oracion) + "\n")

            if(docPreguntaLimpio.similarity(docOracionLimpio) > 0.50):

                # Pasando info al modelo
                result = qa_pipeline({
                    'context': str(oracion),
                    'question': pregunta})

                questionsResult.append(pregunta)
                answersResult.append(result['answer'])

        # Mostrar rsultado final
        print("Preguntas: \n" + str(questionsResult) + "\n" +
              "\n" + "Respuestas: \n" + str(answersResult) + "\n")


# Inicio
gen()
