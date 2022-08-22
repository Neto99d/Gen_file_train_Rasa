import os
import subprocess
import shutil
import entrenarAsistenteES
from pymongo import MongoClient
from datetime import datetime

client = MongoClient()


# BASE DE DATOS
db = client['rasa_File_DB']
# COLECCION USERS
collection = db['bots_virtuales']


def creaAsistente():
    cmd = "rasa init"
    print("Ahora crearemos el Asistente Virtual")
    print("Entre la dirección del directorio o carpeta donde desea crear el Asistente y luego presione ENTER")
    dir = input()
    os.chdir(dir)
    # Insertando datos
    post = {"nombre": "",
            "alojado_en": dir,
            "fecha_creado": datetime.today().strftime('%Y-%m-%d %I:%M')
            }
    post_id = collection.insert_one(post).inserted_id
    print()
    print("El directorio es: ", os.getcwd() + '\n')
    print("Ejecutando comando para crear el Asistente" + '\n')
    print("Rasa le hara una primera pregunta a la que debe responder presionando la tecla ENTER" + '\n')
    print("Rasa le hara una segunda pregunta a la que debe responder presionando la tecla N y luego ENTER" + '\n')
    subprocess.run(cmd)
    print()
    entrenarAsistenteES.entrenar(os.getcwd())
    print()
    print("Ahora podrá conversar con el bot" + '\n')
    subprocess.run("rasa shell")
