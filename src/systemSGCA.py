from pymongo import MongoClient
import bcrypt
from datetime import datetime
import cargaDatos
import socket
import os


client = MongoClient()


# BASE DE DATOS
db = client['rasa_File_DB']
# COLECCION USERS
collection = db['users']


def register():
    print()
    # PIDIENDO DATOS PARA REGISTRO ####
    print()
    print("REGISTRARSE EN EL SISTEMA.")
    name = input('Cree su nombre de usuario : ')
    password = input('Cree su contraseña : ')

    # SI el usuario existe
    existe_user = collection.find_one({'nombre': name})
    if existe_user is None:
        # ENCRIPTAR CONTRASEÑA
        hashpass = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())

        # Insertando datos
        post = {"nombre": name,
                "contraseña": hashpass,
                "fecha_registro": datetime.today().strftime('%Y-%m-%d %I:%M %p'),
                "fechas_Inicio_sesion": []
                }
        post_id = collection.insert_one(post).inserted_id
        print()
        login()
    else:
        print()
        print("Este usuario ya existe. Intente de nuevo" + '\n')
        register()


def login():
    #### PIDIENDO DATOS PARA REGISTRO ####
    print()
    print("INICIAR SESIÓN PARA USAR LA APLICACIÓN")
    name = input('Entre su nombre de usuario : ')
    password = input('Entre su contraseña : ')
    login_user = collection.find_one({'nombre': name})

    if login_user and bcrypt.checkpw(
            password.encode('utf-8'), login_user['contraseña']):

        # Capturando la fecha y hora en que inicia sesion y la IP desde donde se inicia
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        collection.update_one(
            {'nombre': login_user['nombre']}, {
                '$push': {'fechas_Inicio_sesion': datetime.today().strftime('%Y-%m-%d %I:%M %p')+"  IP: " + IPAddr}}
        )
        print()
        os.system("cls")
        cargaDatos.cargaDatos(login_user['nombre'])

    else:
        print()
        print("ERROR de Usuario o contraseña" + '\n')
        opciones()


def opciones():
    print()
   #################################################################
    print("OPCIONES" + "\n" "1. Registrarse" + "\n" "2. Iniciar Sesión")

    no = input("Entre el número de la opción: ")

    if(no == '1'):
        register()
    elif(no == '2'):
        login()
    else:
        print()
        print()
        print("Sólo los valores 1 o 2")
        opciones()


print()
print("Recuerde que los datos entrados para la construcción del conocimiento una vez este dentro del sistema deben ser en Inglés.")
print()
print("A partir de los datos en Inglés se ejecutará el módulo de la herramienta para generar el conocimiento del asistente virtual en idioma español.")
print()
print("- Si desea cancelar cualquier operación y salir a la pantalla principal del Sistema presione Ctrl + C" + "\n" + "- Si le sale al presionar Ctrl +C: " +
          "¿Desea terminar el trabajo por lotes (S/N)?, " + "presione s para cerrar o n para iniciar nuevamente el sistema")
print()

opciones()