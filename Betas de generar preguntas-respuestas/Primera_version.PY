from sentence_transformers import SentenceTransformer, util
from transformers import T5ForConditionalGeneration, T5Tokenizer, BertTokenizer, BertModel, AutoTokenizer, AutoModelForSeq2SeqLM
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import torch
import spacy
from transformers import pipeline
from transformers import BertTokenizer, BertModel
from warnings import filterwarnings as filt


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


texto = '''Código de las Familias es una norma sustantiva del Derecho de Familia en Cuba; Cuerpo legal que regula todas las instituciones relativas a la familia: el matrimonio, el divorcio, las relaciones paterno filiales, la obligación de dar alimentos, la adopción y la tutela. Se promulga en 1975, modificado y propuesto a referendo popular el 25 de septiembre de 2022, siendo ratificado por el pueblo cubano con el 66.87 % de los votos.
Las normas contenidas en este Código se aplican a todas las familias cualquiera que sea la forma de organización que adopten y a las relaciones jurídico-familiares que de ellas se deriven entre sus miembros, y de estos con la sociedad y el Estado y se rigen por los principios, valores y reglas contenidos en la Constitución de la República de Cuba, los tratados internacionales en vigor para el país que tienen incidencia en materia familiar y los previstos en este Código.
Es un Código inclusivo, revolucionario y novedoso en su texto como en su proceso de elaboración. Protege a niños, niñas y adolescentes, les reconoce derechos a las personas adultas mayores y en situación de discapacidad, visibiliza y reconoce derechos a sectores vulnerables, condena la violencia familiar y establece herramientas para los que han sido víctima de ella, condena la discriminación contra la mujer, democratiza las relaciones familiares, le otorga efectos jurídicos al afecto, y reconoce en su articulado la diversidad de realidades que existe entre las familias cubanas.'''

doc = nlp(texto)
sentences = list(doc.sents)
#print(sentences)


def genQuestion():
    print()
    print()
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
        print(Question)
        result = qa_pipeline({
                    'context': str(sent),
                    'question': Question})
        print(result)
        


# Inicio
genQuestion()
