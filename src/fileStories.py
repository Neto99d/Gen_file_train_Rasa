from ruamel.yaml import YAML
import os

GENERATE_FILE = "Archivos_generados"


def storiesYaml(ques, res):  # Recibe preguntas y respuestas
    print('\n' + "Creando archivo de Rasa stories.yml" +
          '\n' '..............................')

    try:
        global auxutter  # Arreglo donde se guardan preguntas y respuestas

        auxutter = []
        #######################################################

        # PLANTILLA para Archivo RASA
        for i in range(len(ques)):
            auxutter.append(
                {"story": 'option ' + str(i + 1),
                 'steps': [{"intent": ques[i]}, {"action": 'utter_{}'.format(ques[i])}]})

        stories = {
            'stories': [{'story': 'camino feliz',
                         'steps': [{'intent': 'saludar'}, {'action': 'utter_saludar'}, {'intent': 'animo'},
                                   {'action': 'utter_feliz'}]},
                        {'story': 'camino triste 1', 'steps': [{'intent': 'saludar'}, {
                            'action': 'utter_saludar'}, {'intent': 'no_animo'}, {'action': 'utter_ayuda'},
                            {'intent': 'afirmar'},
                            {
                            'action': 'utter_feliz'}]},
                        {'story': 'camino triste 2',
                         'steps': [{'intent': 'saludar'}, {'action': 'utter_saludar'}, {'intent': 'no_animo'},
                                   {'action': 'utter_ayuda'}, {
                                       'intent': 'negar'},
                                   {'action': 'utter_adios'}]}]}

        for iUtter in auxutter:
            stories['stories'].append(iUtter)
        versionRasa = {'version': "3.1"}
        #################################################################

        try:
            ################################################
            # Crear el Archivo
            dirname, filename = os.path.split(os.path.abspath(__file__))
            if os.path.exists(dirname + os.path.sep + GENERATE_FILE) == False:
                os.makedirs(dirname + os.path.sep + GENERATE_FILE)
            yaml_file = open(dirname + os.path.sep + GENERATE_FILE + os.path.sep + "stories.yml",
                             mode="w+", encoding="utf-8")

            #########################################
            # Escribiendo la plantilla en el archivo

            yaml = YAML()
            yaml.dump(versionRasa, yaml_file)
            yaml.dump(stories, yaml_file)

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
