from ruamel.yaml import YAML
import os

GENERATE_FILE = "Archivos_generados"


def rulesYaml(ques, res):  # Recibe preguntas y respuestas
    print('\n' + "Creando archivo de Rasa rules.yml" +
          '\n' '..............................')

    try:
        global auxutter  # Arreglo donde se guardan preguntas y respuestas

        auxutter = []

        #######################################################

        # PLANTILLA para Archivo RASA
        for i in range(len(ques)):
            auxutter.append(
                {"rule": 'option ' + str(i + 1),
                 'steps': [{"intent": ques[i]}, {"action": 'utter_{}'.format(ques[i])}]})

        rules = {
            'rules': [{'rule': 'Say goodbye anytime the user says goodbye',
                       'steps': [{'intent': 'goodbye'}, {'action': 'utter_goodbye'}]},
                      {'rule': "Say 'I am a bot' anytime the user challenges",
                       'steps': [{'intent': 'bot_challenge'}, {'action': 'utter_iamabot'}]}]}

        for iUtter in auxutter:
            rules['rules'].append(iUtter)
        versionRasa = {'version': "3.0"}
        #################################################################

        try:
            ################################################
            # Crear el Archivo
            dirname, filename = os.path.split(os.path.abspath(__file__))
            if os.path.exists(dirname + os.path.sep + GENERATE_FILE) == False:
                os.makedirs(dirname + os.path.sep + GENERATE_FILE)
            yaml_file = open(dirname + os.path.sep + GENERATE_FILE + os.path.sep + "rules.yml",
                             mode="a+")

            #########################################
            # Escribiendo la plantilla en el archivo

            yaml = YAML()
            yaml.dump(versionRasa, yaml_file)
            yaml.dump(rules, yaml_file)

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
