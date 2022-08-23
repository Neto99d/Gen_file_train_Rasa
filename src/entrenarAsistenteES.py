import shutil
import os



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
        print("Archivos movidos a la carpeta del Asistente para ser entrenado" + '\n')
        return True

    except Exception as error:
        print(error)
        print("Error: No existe uno de los archivos de entrenamiento, o ninguno")
        print("Ejecute la herramienta nuevamente")
        return False


def entrenar(direccionBot):
    visualConocimiento = "rasa visualize"
    train = "rasa train"
    print()
    print("Ahora entrenaremos al Asistente")
    global dir
    dir = direccionBot
    os.chdir(direccionBot)
    print()
    print("El directorio dónde está su Asistente Virtual es: ", os.getcwd())
    print()
    if mover():
        print("Entrenando al Asistente")
        print("Espere......... Esta cargando....")
        os.system(train)
        print()
        print("Se le mostrará un gráfico en su navegador donde podrá ver las preguntas y las respuestas inferidas a cada pregunta (utter_pregunta) después del entrenamiento, para verificar que el Asistente tendrá alta probabilidad de responder correctamente.")
        os.system(visualConocimiento)
        
