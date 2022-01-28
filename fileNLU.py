import ruamel.yaml
from ruamel.yaml.scalarstring import PreservedScalarString as literal_
import os

GENERATE_FILE = "Archivos_generados";

literal = literal_  # Forma literal Yaml multilinea  | ó |-


def nluYaml(ques, res):  # Recibe preguntas y respuestas
    print('\n' + "Creando archivo de Rasa nlu.yml" + '\n' '..............................')

    try:
        global auxutter  # Arreglo donde se guardan preguntas y respuestas

        auxutter = []

        #######################################################

        # PLANTILLA para Archivo RASA
        for i in range(len(ques)):
            auxutter.append({"intent": ques[i], 'examples': literal('- ' + ques[i])})

        nlu = {
            'nlu':
                [{'intent': 'greet',
                  'examples': literal_('\n'.join(['- hey',
                                                  '- hello',
                                                  '- hi',
                                                  '- hello there',
                                                  '- good morning',
                                                  '- good evening']) + '\n')
                  },

                 {'intent': 'goodbye',
                  'examples': literal_('\n'.join(['- good bye',
                                                  '- good night',
                                                  '- bye',
                                                  '- goodbye',
                                                  '- bye bye',
                                                  '- see you later']) + '\n')},

                 {'intent': 'affirm',
                  'examples': literal_('\n'.join(['- yes',
                                                  '- of course',
                                                  '- correct']) + '\n')},

                 {'intent': 'deny',
                  'examples': literal_('\n'.join(['- no',
                                                  '- never',
                                                  '- no way',
                                                  '- not really']) + '\n')},

                 {'intent': 'mood_great',
                  'examples': literal_('\n'.join(['- perfect',
                                                  '- great',
                                                  '- amazing',
                                                  '- I am feeling very good',
                                                  '- I am great',
                                                  '- I am amazing',
                                                  '- I am going to save the world',
                                                  '- I am ok',
                                                  '- ok']) + '\n')},

                 {'intent': 'mood_unhappy',
                  'examples': literal_('\n'.join(['- my day was horrible',
                                                  '- I am sad',
                                                  '- I am disappointed',
                                                  '- super sad',
                                                  '- I am so sad',
                                                  '- sad',
                                                  '- very sad',
                                                  '- unhappy',
                                                  '- not good']) + '\n')},

                 {'intent': 'bot_challenge',
                  'examples': literal_('\n'.join(['- are you a bot?',
                                                  '- are you a human?',
                                                  '- am I talking to a bot?',
                                                  '- am I talking to a human?']) + '\n')},

                 ]
        }

        for iUtter in auxutter:
            nlu['nlu'].append(iUtter)
        versionRasa = {'version': "3.0"}

        #################################################################

        try:
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

                yaml = ruamel.yaml.YAML()
                yaml.indent(mapping=2, sequence=3, offset=1)  # Sangria y margen
                yaml.dump(versionRasa, yaml_file)
                yaml.dump(nlu, yaml_file)

                ############################################
                # Validacion para posibles errores
        except Exception as error:
            print("Error al crear archivo o se creó pero está mal")
            print("Error: ", error)

    except Exception as error:
        print("Error al crear plantilla, archivo Rasa no creado")
        print("Error: ", error)
#######################################################################
