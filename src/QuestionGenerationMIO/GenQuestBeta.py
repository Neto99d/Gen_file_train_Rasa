import spacy
from spacy import displacy

# modelo de spacy
nlp = spacy.load("es_core_news_md")

# textos de ejemplo

texto = '''El presidente de Cuba, Miguel Díaz-Canel, felicitó a profesores y estudiantes de la Universidad de Oriente por su aniversario 75. A través de Twitter, el mandatario resaltó el aporte pedagógico y científico de la segunda institución superior pública del país.

Asimismo, el titular de la Asamblea Nacional del Poder Popular (parlamento), Esteban Lazo, al saludar la efeméride, extendió sus parabienes a los graduados de la institución educativa.

Por su parte, la ministra de Educación, Ena Elsa Velázquez, calificó en una misiva a esa casa de altos estudios de baluarte de la dignidad del estudiantado universitario oriental, distinguidos por su consagración al estudio, su talento, profesionalidad y disciplina.

Nos enorgullece saber este recinto como líder de proyectos de investigación. Transformar, aportar y crear ha sido siempre la misión de ustedes, sello que ha marcado la calidad del joven que de aquí egresa, apuntó.

Destacó que “miles han sido los graduados en estos años, sobre todo después del triunfo revolucionario (1 de enero de 1959), donde la universidad se abanderó como popular y se abrió a todos como institución necesaria para la superación del pueblo”.

Fundada en 1947, en Santiago de Cuba, la Universidad de Oriente es una institución de carácter público, dedicada a la educación e investigación a nivel superior y postgrado.'''

texto2 = '''Código de las Familias. Norma sustantiva del Derecho de Familia en Cuba. Cuerpo legal que regula todas las instituciones relativas a la familia: el matrimonio, el divorcio, las relaciones paterno filiales, la obligación de dar alimentos, la adopción y la tutela. Se promulga en 1975, modificado y propuesto a referendo popular el 25 de septiembre de 2022, siendo ratificado por el pueblo cubano con el 66.87 % de los votos.
Las normas contenidas en este Código se aplican a todas las familias cualquiera que sea la forma de organización que adopten y a las relaciones jurídico-familiares que de ellas se deriven entre sus miembros, y de estos con la sociedad y el Estado y se rigen por los principios, valores y reglas contenidos en la Constitución de la República de Cuba, los tratados internacionales en vigor para el país que tienen incidencia en materia familiar y los previstos en este Código.
Es un Código inclusivo, revolucionario y novedoso en su texto como en su proceso de elaboración. Protege a niños, niñas y adolescentes, les reconoce derechos a las personas adultas mayores y en situación de discapacidad, visibiliza y reconoce derechos a sectores vulnerables, condena la violencia familiar y establece herramientas para los que han sido víctima de ella, condena la discriminación contra la mujer, democratiza las relaciones familiares, le otorga efectos jurídicos al afecto, y reconoce en su articulado la diversidad de realidades que existe entre las familias cubanas.'''

texto3 = '''Criptomoneda es una moneda-virtual para asegurar transacciones.
Bitcoin es una criptodivisa descentralizada.
Digital-Wallet es una aplicación donde es posible almacenar, enviar y recibir criptomonedas.
La Ciudad-Inteligente es un tipo de desarrollo urbano basado en la sostenibilidad para las necesidades básicas de instituciones, empresas y de los propios habitantes.'''

#### DOCUMENTOS SAPCY ###########

# doc = nlp(texto)
# doc = nlp(texto2)
doc = nlp(texto3)

# Lista de oraciones del texto
sentences = list(doc.sents)

# arreglo para guardar las preguntas
questions = []


def genQuest(sentence):
    docSent = nlp(str(sentence))
    formaverbal = ""
    formaVerbalAUX = ""
    verbo = ""
    organizacion = ""
    personaje = ""
    print()
    # displacy.render(docSent, style="dep") para ver en jupyter
    print()

    # Extrayendo verbos, formas verbales al tokenizar la oracion
    for tok in docSent:
        # print(tok.text, tok.tag_, tok.dep_)
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
            questions.append('Que es {}'.format(ent.text))
        elif(ent.label_ == "PER"):
            personaje = ent.text
            questions.append('Quien es {}'.format(ent.text))
        elif(ent.label_ == "ORG"):
            organizacion = ent.text
            questions.append('Que paso en {}'.format(ent.text))
            questions.append('Quienes integran {}'.format(ent.text))
            if(formaverbal != ""):
                # pasando la forma verbal que puede verse como la accion que se ejecuto en la organizacion
                questions.append('Quien {}'.format(formaverbal))
                # questions.append('A quien {}'.format(formaverbal))
        # Si se habla en la misma oracion sobre una persona y una organizacion
        if(organizacion != "" and personaje != ""):
            questions.append('Que significa o representa {} para {}'.format(
                personaje, organizacion))
        elif(ent.label_ == "LOC"):
            questions.append('Que paso en {}'.format(ent.text))
            questions.append('Que es {}'.format(ent.text))
            questions.append('Donde queda {}'.format(ent.text))

    print("FIN DE ENTIDADES")
    print()
    print("PREGUNTAS")

    # eliminar duplicados
    questionsFIX = set(questions)

    # Mostrar preguntas
    print(questionsFIX)


# Enviando cada oracion a la funcion de generar pregunta
for sent in sentences:
    genQuest(sent)
