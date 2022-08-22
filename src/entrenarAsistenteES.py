import shutil
import os
import ConfigToSpacyNLP_ES


def mover():
    try:
        print()
        dirname, filename = os.path.split(os.path.abspath(__file__))
        #######################################
        print()
        print("Moviendo Archivos..........." + '\n')

        shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "domain.yml",
                    os.path.join(dir, "domain.yml"))
        shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "nlu.yml",
                    os.path.join(dir + "\data", "nlu.yml"))
        shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "stories.yml",
                    os.path.join(dir + "\data", "stories.yml"))
        shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "rules.yml",
                    os.path.join(dir + "\data", "rules.yml"))
        # shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "config.yml",
                    # os.path.join(dir, "config.yml"))
        print("Archivos movidos a la carpeta del Asistente para ser entrenado" + '\n')
        return True

    except Exception as error:
        print(error)
        print("Error: No existe uno de los archivos de entrenamiento, o ninguno")
        print("Ejecute la herramienta nuevamente")
        return False


def entrenar(direccionBot):
    # spacy = ConfigToSpacyNLP_ES
    # spacy.configYaml()
    train = "rasa train"
    print()
    print("Ahora entrenaremos al Asistente")
    # print("Entre la direccion del directorio donde esta el Asistente y luego presione ENTER")
    global dir
    dir = direccionBot
    os.chdir(direccionBot)
    print()
    print("El directorio dónde está su Asistente Virtual es: ", os.getcwd())
    if mover():
        print("Entrenando al Asistente")
        print("Espere......... Esta cargando....")
        os.system(train)
