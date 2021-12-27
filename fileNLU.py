import yaml as ym  # PYyaml
import sys
from ruamel.yaml import YAML  # Ramuel.yaml
import os
from collections import defaultdict

GENERATE_FILE = "Archivos_generados";


def nluYaml(ques, res):  # Recibe preguntas y respuestas
    print('\n' + "Creando archivo de Rasa nlu.yml" + '\n' '..............................')

    try:
        global auxutter  # Arreglo donde se guardan preguntas y respuestas

        auxutter = []

        #######################################################

        # PLANTILLA para Archivo RASA
        for i in range(len(ques)):
            auxutter.append({"intent": ques[i], 'examples': [ques[i]]})
        toPrintYaml = dict()
        for element in auxutter:
            for key, value in element.items():
                toPrintYaml[key] = value
        print(toPrintYaml)
        nlu = {
            'nlu':
                [{'intent': 'greet',
                  'examples': ['hey',
                               'hello',
                               'hi',
                               'hello there',
                               'good morning',
                               'good evening']
                  },

                 {'intent': 'goodbye',
                  'examples': ['good bye',
                               'good night',
                               'bye',
                               'goodbye',
                               'bye bye',
                               'see you later']},

                 {'intent': 'affirm',
                  'examples': ['yes',
                               'of course',
                               'correct']},

                 {'intent': 'deny',
                  'examples': ['no',
                               'never',
                               'no way',
                               'not really']},

                 {'intent': 'mood_great',
                  'examples': ['perfect',
                               'great',
                               'amazing',
                               'I am feeling very good',
                               'I am great',
                               'I am amazing',
                               'I am going to save the world',
                               'I am ok',
                               'ok']},

                 {'intent': 'mood_unhappy',
                  'examples': ['my day was horrible',
                               'I am sad',
                               'I am disappointed',
                               'super sad',
                               'I am so sad',
                               'sad',
                               'very sad',
                               'unhappy',
                               'not good']},

                 {'intent': 'bot_challenge',
                  'examples': ['are you a bot?',
                               'are you a human?',
                               'am I talking to a bot?',
                               'am I talking to a human?']}
                 ]
        }

        versionRasa = {'version': "3.0"}
        #################################################################

        try:
            ################################################
            # Crear el Archivo
            dirname, filename = os.path.split(os.path.abspath(__file__))
            if os.path.exists(dirname + os.path.sep + GENERATE_FILE) == False:
                os.makedirs(dirname + os.path.sep + GENERATE_FILE)
            yaml_file = open(dirname + os.path.sep + GENERATE_FILE + os.path.sep + "nlu.yml",
                             mode="a+")
            if yaml_file:
                print(
                    '\n' + "Creado con Exito, en la carpeta Archivos_generados" + '\n' '..............................')
                print(
                    "Por favor una vez que copie los archivos generados en la carpeta de entrenamiento del bot de Rasa "
                    ">>> Elimine los archivos de la carpeta Archivos_generados")

                #########################################
                # Escribiendo la plantilla en el archivo

                yaml = YAML()
                #   # Sangria y margen
                yaml.dump(versionRasa, yaml_file)
                yaml.indent(mapping=2, sequence=2)
                yaml.dump(nlu, yaml_file)
                # yaml = YAML()
                # Guardando la info de repsonses

                # toPrintYaml = dict()
                # for element in auxutter:        # Poniendo informacion en un diccionario, clave = valor
                # for key, value in element.items():
                # toPrintYaml[key] = value

                # for element in utterSaludo:
                # for key, value in element.items():
                # toPrintYaml[key] = value

                ############################################
                # Validacion para posibles errores
        except Exception as error:
            print("Error al crear archivo o se creó pero está mal")
            print("Error: ", error)

    except Exception as error:
        print("Error al crear plantilla, archivo Rasa no creado")
        print("Error: ", error)
#######################################################################
