import yaml
import sys


def modYaml(ques, res):  # Recibe preguntas y respuestas
    print('\n' + "Creando archivo de Rasa domain.yml" + '\n' '..............................')

    try:
        global auxres, auxutter # Arreglo donde se guardan preguntas y respuestas
        auxres = []
        auxutter = []
        ##########################################
        # PLANTILLA para Archivo RASA

        versionRasa = {'version': "3.0"}
        intent = {'intents': ques}
        for i in range(len(ques)):
            for i in range(len(res)):
                auxutter.append({'utter_' + ques[i]: [{'text': res[i]}]})
                break
            # auxres.append({'utter_' + ques[i]: [{'text': res[i]}]})
        config = {'session_config': {
            'session_expiration_time': 60,
            'carry_over_slots_to_new_session': True, }
        }
        #################################################################

        try:
            ################################################
            # Crear el Archivo y escribir la plantilla en el mismo

            yaml_file = open("D:\\DOCUMENTOS\\VisualStudio_Projects\\GitHub\\genquest\\Archivos_generados\\domain.yml",
                             mode="a")
            if yaml_file:
                print(
                    '\n' + "Creado con Exito, en la carpeta Archivos_generados" + '\n' '..............................')
                print(
                    "Por favor corte y pegue los archivos en la carpeta de entrenamiento. No deje los archivos en la carpeta")

            #########################################
            # Escribiendo la plantilla en el archivo

            yaml.dump(versionRasa, yaml_file)
            yaml.dump(intent, yaml_file)
            yaml.dump({'_responses': ""}, yaml_file)
            yaml.dump({'responses': auxutter}, yaml_file)
            yaml.dump(config, yaml_file)
        ##########################################

        ############################################
        # Validacion para posibles errores
        except Exception as error:
            print("Error al crear archivo")
            print(error)

    except Exception as error:
        print("Error al crear plantilla, archivo Rasa no creado")
        print(error)
#######################################################################
