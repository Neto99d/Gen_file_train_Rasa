import numpy as np
from sentence_transformers import SentenceTransformer, util
import spacy
from spacy import displacy
from collections import OrderedDict
from sentence_transformers import SentenceTransformer

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


# Modelo calculo de Similitud entre oraciones
model = SentenceTransformer("eduardofv/stsb-m-mt-es-distilbert-base-uncased") 





# textos de ejemplo

texto = '''Código de las Familias es la norma sustantiva del Derecho de Familia en Cuba. Cuerpo legal que regula todas las instituciones relativas a la familia: el matrimonio, el divorcio, las relaciones paterno filiales, la obligación de dar alimentos, la adopción y la tutela. Se promulga en 1975, modificado y propuesto a referendo popular el 25 de septiembre de 2022, siendo ratificado por el pueblo cubano con el 66.87 % de los votos.
Las normas contenidas en este Código se aplican a todas las familias cualquiera que sea la forma de organización que adopten y a las relaciones jurídico-familiares que de ellas se deriven entre sus miembros, y de estos con la sociedad y el Estado y se rigen por los principios, valores y reglas contenidos en la Constitución de la República de Cuba, los tratados internacionales en vigor para el país que tienen incidencia en materia familiar y los previstos en este Código.
Es un Código inclusivo, revolucionario y novedoso en su texto como en su proceso de elaboración. Protege a niños, niñas y adolescentes, les reconoce derechos a las personas adultas mayores y en situación de discapacidad, visibiliza y reconoce derechos a sectores vulnerables, condena la violencia familiar y establece herramientas para los que han sido víctima de ella, condena la discriminación contra la mujer, democratiza las relaciones familiares, le otorga efectos jurídicos al afecto, y reconoce en su articulado la diversidad de realidades que existe entre las familias cubanas.'''


#### DOCUMENTOS SAPCY ###########
doc = nlp(texto)


# Lista de oraciones del texto
sentences = list(doc.sents)
sentencesSTR = []
# print(str(sentences))
# arreglo para guardar las preguntas
questions = []
questionsResult = []
answersResult = []



def genQuest():
    for sent in sentences:
        sentencesSTR.append(str(sent))  # Coger las oraciones en String
        docSent = nlp(str(sent))
        formaverbal = ""
        formaVerbalAUX = ""
        verbo = ""
        organizacion = ""
        personaje = ""
        print()
        #displacy.render(docSent, style="dep")  # para ver en jupyter
        print()

        # Extrayendo verbos, formas verbales al tokenizar la oracion
        for tok in docSent:
            #print(tok.text, tok.tag_, tok.dep_, tok.pos_)
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
            #print(ent.text, ent.start_char, ent.end_char, ent.label_)

            # Creando la pregunta de acuerdo al tipo de entidad y guardando las preguntas en un arreglo
            if(ent.label_ == "MISC"):
                if not ent.text in ["Twitter", "Facebook", "Instagram", "Linkedin", "Youtube", "Telegram"]:
                    questions.append('Qué es {}'.format(ent.text))
            elif(ent.label_ == "PER"):
                personaje = ent.text
                questions.append('Quién es {}'.format(ent.text))
            elif(ent.label_ == "ORG"):
                organizacion = ent.text
                questions.append('Qué paso en o con {}'.format(ent.text))
                questions.append('Quiénes integran {}'.format(ent.text))
                if(formaverbal != "" and organizacion != "" and personaje != ""):
                    # pasando la forma verbal que puede verse como la accion que se ejecuto en la organizacion
                    questions.append('Quién {}'.format(
                        formaverbal) + " en {}".format(organizacion))
                # questions.append('A quien {}'.format(formaverbal))
            # Si se habla en la misma oracion sobre una persona y una organizacion
            if(organizacion != "" and personaje != ""):
                questions.append('Quién es {} para {}'.format(
                    personaje, organizacion))
            elif(ent.label_ == "LOC"):
                #questions.append('Que paso en {}'.format(ent.text))
                questions.append('Qué es {}'.format(ent.text))
                questions.append(
                    'Dónde queda {}'.format(ent.text))
            print()
        # print("FIN DE ENTIDADES")
        print()

    # eliminar duplicados
    questionsFIX = set(questions)
    print("PREGUNTAS")
    # Mostrar preguntas
    print(questionsFIX)
    # LLamada
    analisiSimilitud(questionsFIX)


def analisiSimilitud(questions):
    print()
    print()
    print("ANALIZANDO similitud de las preguntas con las oraciones")
    print()
    top_k = 1
    # encode corpus to get corpus embeddings
    corpus_embeddings = model.encode(sentencesSTR, convert_to_tensor=True)
    for pregunta in questions:
        print()
        embedding1 = model.encode(pregunta, convert_to_tensor=True)

        # compute similarity scores of the sentence with the corpus
        cos_scores = util.pytorch_cos_sim(
            embedding1, corpus_embeddings)[0]

        # Sort the results in decreasing order and get the first top_k
        top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]

        print("Sentence:", pregunta, "\n")
        print("Top", top_k, "most similar sentences in corpus:")
        for idx in top_results[0:top_k]:
            print(sentencesSTR[idx], "(Score: %.4f)" % (cos_scores[idx]))
            result = qa_pipeline({
                    'context': sentencesSTR[idx],
                    'question': pregunta})
            questionsResult.append(pregunta)
            answersResult.append(result['answer'])

    print() 
    # Mostrando resultado final
    print("Preguntas: " + str(questionsResult) + "\n" +
          "\n" + "Respuestas: " + str(answersResult))
    print(len(questionsResult), len(answersResult))
    

# Inicio
genQuest()
