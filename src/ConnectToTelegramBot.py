from ruamel.yaml import YAML
import os
import shutil


GENERATE_FILE = "Archivos_generados"


def credentYaml():  
    print()
    print("Archivo necesario para conectar su Asistente a su bot de Telegram para que pueda interactuar con él desde esa plataforma")
    print('\n' + "Creando archivo de Rasa credentials.yml" +
          '\n' '..............................')

    try:
        #######################################################
        # PLANTILLA para Archivo RASA
        rest = {'rest': None}
        socketIO = {'socketio': {'user_message_evt': 'user_uttered',
                                 'bot_message_evt': 'bot_uttered', 'session_persistence': 'false'}}
        rasa = {'rasa': {'url': 'http://localhost:5002/api'}}
        telegram = {'telegram': {'access_token': None,
                                 'verify': None, 'webhook_url': None}}

        #################################################################

        try:
            # Crear el Archivo
            dirname, filename = os.path.split(os.path.abspath(__file__))
            if os.path.exists(dirname + os.path.sep + GENERATE_FILE) == False:
                os.makedirs(dirname + os.path.sep + GENERATE_FILE)
            yaml_file = open(dirname + os.path.sep + GENERATE_FILE + os.path.sep + "credentials.yml",
                             mode="w+")

            #########################################
            # Escribiendo la plantilla en el archivo

            yaml = YAML()
            yaml.indent(mapping=2, sequence=4, offset=2)  # Sangria y margen
            yaml.dump(rest, yaml_file)
            yaml.dump(socketIO, yaml_file)
            yaml.dump(rasa, yaml_file)
            print()
            print("Para conectar su Asistente a su bot de Telegram")
            print("Entre el token de su bot de Telegram: ")
            token = input()
            print(
                "Entre el nombre de usuario (sin el @) que aparece en el perfil (no el nombre normal) de su bot de Telegram: ")
            nombre = input()
            print(
                "Entre la direccion Webhook desde donde recibirá las peticiones (Solo https): ")
            webhook = input()

            telegram['telegram']['access_token'] = token
            telegram['telegram']['verify'] = nombre
            telegram['telegram']['webhook_url'] = webhook + \
                "/webhooks/telegram/webhook"
            yaml.dump(telegram, yaml_file)
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


if credentYaml():
    print()
    print("Creado con Exito :)" + '\n')
    try:
        dirname, filename = os.path.split(os.path.abspath(__file__))
        print("Se moverá el archivo a la carpeta del Asistente")
        print(
            "Entre la direccion del directorio o carpeta donde esta el Asistente y luego presione ENTER")
        dir = input()
        os.chdir(dir)
        print()
        print("El directorio es: ", os.getcwd() + '\n')
        print("Moviendo Archivo..........." + '\n')
        shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "credentials.yml",
                    os.path.join(dir, "credentials.yml"))
        print("Movido con Exito :)")
        print()
        print("Operacón para la configuración de conexión con Telegram-Bot finalizada con éxito")
    except Exception as error:
        print()
        print("Error: No existe el archivo")
