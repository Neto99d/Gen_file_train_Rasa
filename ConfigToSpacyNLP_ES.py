from ruamel.yaml import YAML
import os
import shutil

GENERATE_FILE = "Archivos_generados"


def configYaml():
    print()
    print("Archivo necesario para analizar con el idioma español")
    print('\n' + "Creando archivo de Rasa config.yml" +
          '\n' '..............................')

    try:
        #######################################################
        # PLANTILLA para Archivo RASA
        recipe = {"recipe": "default.v1"}
        pipeline = {'pipeline': [{'name': 'SpacyNLP', 'model': 'es_core_news_md'}, {'name': 'SpacyTokenizer'},
                                 {'name': 'SpacyFeaturizer'}, {'name': 'RegexFeaturizer'},
                                 {'name': 'CRFEntityExtractor'}, {'name': 'EntitySynonymMapper'},
                                 {'name': 'SklearnIntentClassifier'}]}
        idioma = {'language': 'es'}
        policies = {'policies': None}

        #################################################################

        try:
            # Crear el Archivo
            dirname, filename = os.path.split(os.path.abspath(__file__))
            if os.path.exists(dirname + os.path.sep + GENERATE_FILE) == False:
                os.makedirs(dirname + os.path.sep + GENERATE_FILE)
            yaml_file = open(dirname + os.path.sep + GENERATE_FILE + os.path.sep + "config.yml",
                             mode="a+")

            #########################################
            # Escribiendo la plantilla en el archivo

            yaml = YAML()
            yaml.indent(mapping=2, sequence=4, offset=2)  # Sangria y margen
            yaml.dump(recipe, yaml_file)
            yaml.dump(idioma, yaml_file)
            yaml.dump(pipeline, yaml_file)
            yaml.dump(policies, yaml_file)

        ############################################
        # Validacion para posibles errores
        except Exception as error:
            print("Error al crear archivo o se creó pero está mal")
            print("Error: ", error)
        return True
    except Exception as error:
        print("Error al crear plantilla, archivo Rasa no creado")
        print("Error: ", error)
        return False

#######################################################################
