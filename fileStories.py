import yaml
import sys



def modYaml(ques, res):  # Recibe preguntas y respuestas
    print('\n' + "Creando archivo de Rasa stories.yml" + '\n' '..............................')

    try:
        global auxres  # Arreglo donde se guardan preguntas y respuestas
        auxres = []

        ##################################################
        # Bucle para guardar pares de preguntas y respuestas

        for i in range(len(ques)):
            for i in range(len(res)):
                auxres.append({'utter_' + ques[i]: [{'text': res[i]}]})  # se guarda la pregunta: respuesta
            break  # Para impedir que haga doble la busqueda o siga (no es infinito pero sale repetido)

        ##########################################
        # PLANTILLA para Archivo RASA

        domain = {
            'version': "3.0",

            'intents': ques,  # preguntas

            'responses': auxres,  # utter_preguntas: text_respuestas

            'session_config': {
                'session_expiration_time': 60,
                'carry_over_slots_to_new_session': True, }
        }
        #################################################################

        try:
            ################################################
            # Crear el Archivo y escribir la plantilla en el mismo
            yaml_file = open("D:\\DOCUMENTOS\\VisualStudio_Projects\\GitHub\\genquest\\Archivos_generados\\stories.yml",
                             mode="a")
            if yaml_file:
                print(
                    '\n' + "Creado con Exito, en la carpeta Archivos_generados" + '\n' '..............................')
                print(
                    "Por favor corte y pegue los archivos en la carpeta de entrenamiento. No deje los archivos en la carpeta")
            yaml.dump(domain, yaml_file)
            # yaml.dump(domain, sys.stdout)

        ############################################
        # Validacion para posibles errores
        except Exception as error:
            print("Error al crear archivo")
            print(error)

    except Exception as error:
        print("Error al crear plantilla, archivo Rasa no creado")
        print(error)
    #######################################################################