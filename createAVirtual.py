import os, subprocess
# import entrenarAsistente


def creaAsistente():
    cmd = "rasa init"
    # entrenar = entrenarAsistente
    print("Entre la direccion del directorio donde desea crear el Asistente y luego presione ENTER")
    dir = input()
    os.chdir(dir)
    print()
    print("El directorio es: ", os.getcwd())
    print()
    print("Ejecutando comando para crear el Asistente")
    print()
    print("Rasa le hara una primera pregunta a la que debe responder presionando la tecla ENTER")
    print()
    print("Rasa le hara una segunda pregunta a la que debe responder presionando la tecla N y luego ENTER")
    print()
    subprocess.run(cmd)
    # entrenar.entrenar()

creaAsistente()