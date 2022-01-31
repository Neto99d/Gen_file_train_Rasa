from ruamel.yaml import YAML
import os

GENERATE_FILE = "Archivos_generados";


def domYaml(ques, res):  # Recibe preguntas y respuestas
    print('\n' + "Creando archivo de Rasa domain.yml" + '\n' '..............................')

    try:
        global auxutter  # Arreglo donde se guardan preguntas y respuestas

        auxutter = []

        #######################################################
        # PLANTILLA para Archivo RASA
        saludo = ['greet', 'goodbye',
                  'affirm',
                  'deny',
                  'mood_great',
                  'mood_unhappy',
                  'bot_challenge']
        utterSaludo = [{'utter_greet':
                            [{'text': "Hey! How are you?"}]},

                       {'utter_did_that_help':
                            [{'text': "Did that help you?"}]},

                       {'utter_happy':
                            [{'text': "Great, carry on!"}]},

                       {'utter_goodbye':
                            [{'text': "Bye"}]},

                       {'utter_iamabot':
                            [{'text': "I am a bot, powered by Rasa."}]}]
        versionRasa = {'version': "3.0"}
        intent = {'intents': saludo + ques}
        config = {'session_config': {
            'session_expiration_time': 60,
            'carry_over_slots_to_new_session': True, }
        }
        #################################################################

        try:
            # Crear el Archivo
            dirname, filename = os.path.split(os.path.abspath(__file__))
            if os.path.exists(dirname + os.path.sep + GENERATE_FILE) == False:
                os.makedirs(dirname + os.path.sep + GENERATE_FILE)
            yaml_file = open(dirname + os.path.sep + GENERATE_FILE + os.path.sep + "domain.yml",
                             mode="a+")

            #########################################
            # Escribiendo la plantilla en el archivo

            yaml = YAML()
            yaml.indent(mapping=2, sequence=4, offset=2)  # Sangria y margen
            yaml.dump(versionRasa, yaml_file)
            yaml.dump(intent, yaml_file)
            yaml = YAML()
            for i in range(len(ques)):
                auxutter.append({'utter_{}'.format(ques[i]): [{'text': res[i]}]})  # Guardando la info de repsonses

            toPrintYaml = dict()
            for element in utterSaludo:  # Poniendo informacion en un diccionario, clave = valor
                for key, value in element.items():
                    toPrintYaml[key] = value

            for element in auxutter:  # Poniendo informacion en un diccionario, clave = valor
                for key, value in element.items():
                    toPrintYaml[key] = value

                yaml.dump(dict({'responses': toPrintYaml}), yaml_file)
                yaml.dump(config, yaml_file)

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
