import os
import subprocess
import shutil
import entrenarAsistente


def creaAsistente():
    cmd = "rasa init"
    print("Ahora crearemos el Asistente Virtual")
    print("Entre la direccion del directorio donde desea crear el Asistente y luego presione ENTER")
    dir = input()
    os.chdir(dir)
    print()
    print("El directorio es: ", os.getcwd() + '\n')
    print("Ejecutando comando para crear el Asistente" + '\n')
    print("Rasa le hara una primera pregunta a la que debe responder presionando la tecla ENTER" + '\n')
    print("Rasa le hara una segunda pregunta a la que debe responder presionando la tecla N y luego ENTER" + '\n')
    subprocess.run(cmd)
    print()
    entrenarAsistente.entrenar()
    print()
    print("Ahora podrá conversar con el bot" + '\n')
    subprocess.run("rasa shell")
