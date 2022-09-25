import os
import subprocess
import shutil
import entrenarAsistenteES
from pymongo import MongoClient
from datetime import datetime
import cargaDatos

client = MongoClient()


# BASE DE DATOS
db = client['rasa_File_DB']
# COLECCION de asistentes virtuales
collection = db['asistentes_virtuales']


def opcion(user):
    confirmar = input(
        "Desea crear otro Asistente: Escriba si o no: ")
    if (confirmar == 'si'):
            print()
            creaAsistente(user)
    else:
        print()
        os.system("cls")
        cargaDatos.cargaDatos(user)
        
###################################################     
  
def creaAsistente(user):  # Recibe el usuario logueado
    cmd = "rasa init"
    print("Ahora crearemos el Asistente Virtual")
    print()
    print("Entre un nombre para su asistente virtual")
    nombre = input()
    existe_asistente = collection.find_one({'nombre': nombre})
    if existe_asistente is None:
        print()
        print(
            "Entre una descripción sobre su asistente, algo así como el propósito del mismo")
        descripcion = input()
        print()
        print("Entre la dirección del directorio o carpeta donde desea crear el Asistente y luego presione ENTER")
        dir = input()
        os.chdir(dir)
        # Insertando datos
        post = {"nombre": nombre,
                "descripcion": descripcion,
                "creado_por": user,
                "alojado_en": dir,
                "entrenado": False,
                "fecha_creado": datetime.today().strftime('%Y-%m-%d %I:%M %p')
                }
        post_id = collection.insert_one(post).inserted_id
        print()
        print("El directorio es: ", os.getcwd() + '\n')
        print("Ejecutando comando para crear el Asistente" + '\n')
        print("Rasa le hara una primera pregunta a la que debe responder presionando la tecla ENTER" + '\n')
        print("Rasa le hara una segunda pregunta a la que debe responder presionando la tecla N" + '\n')
        subprocess.run(cmd)  # CREANDO ASISTENTE
        print()
        os.system("cls")
        opcion(user)
    else:
        print()
        print("Este nombre ya existe en uno de los asistentes. Intente de nuevo" + '\n')
        creaAsistente(user)



