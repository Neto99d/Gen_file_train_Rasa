import yaml as ym  # PYyaml
import sys
from ruamel.yaml import YAML  # Ramuel.yaml


def modYaml(ques, res):  # Recibe preguntas y respuestas
    print('\n' + "Creando archivo de Rasa domain.yml" + '\n' '..............................')

    try:
        global auxutter  # Arreglo donde se guardan preguntas y respuestas

        auxutter = []

        #######################################################
        # PLANTILLA para Archivo RASA

        versionRasa = {'version': "3.0"}
        intent = {'intents': ques}
        # responses = {
        # 'responses': None}  # {'responses': {'utter_{}'.format(ques[0]): [{'text': res[0]}]}} # escrito directamente sin lista, solo un elemento ( escribir una a una) INCOMPLETO
        config = {'session_config': {
            'session_expiration_time': 60,
            'carry_over_slots_to_new_session': True, }
        }
        #################################################################

        try:
            ################################################
            # Crear el Archivo

            yaml_file = open(
                ".\\Archivos_generados\\domain.yml",
                mode="a+")
            if yaml_file:
                print(
                    '\n' + "Creado con Exito, en la carpeta Archivos_generados" + '\n' '..............................')
                print(
                    "Por favor corte y pegue los archivos en la carpeta de entrenamiento. No deje los archivos en la carpeta")

            #########################################
            # Escribiendo la plantilla en el archivo

            yaml = YAML()
            yaml.indent(mapping=2, sequence=4, offset=2)  # Sangria y margen
            yaml.dump(versionRasa, yaml_file)
            yaml.dump(intent, yaml_file)
            yaml = YAML()
            for i in range(len(ques)):
                auxutter.append({'utter_{}'.format(ques[i]): [{'text': res[i]}]})  # Guardando la info de repsonses
            yaml.dump({'responses': auxutter}, yaml_file)  # Escrito con la lista donde esta la info
            yaml.dump(config, yaml_file)

            ##########################################

            # f = open('.\\Temporal files\\utter.yml', 'a+')
            # f.writelines(["%s\n" % item for item in auxutter])
            # f =  open('.\\Archivos_generados\\domain.yml', 'r')
            # code = yaml.load(f)
            # for i in range(len(ques)):
            # code['responses'] = {'utter_{}'.format(ques[i]): [{'text': res[i]}]}
            # yaml.dump(code, yaml_file)

            ############################################
            # Validacion para posibles errores
        except Exception as error:
            print("Error al crear archivo o se creó pero está mal")
            print("Error: ", error)

    except Exception as error:
        print("Error al crear plantilla, archivo Rasa no creado")
        print("Error: ", error)
#######################################################################
