from pymongo import MongoClient
import bcrypt
from datetime import datetime
import cargaDatos
import getpass
import socket
import os


client = MongoClient()


# BASE DE DATOS
db = client['rasa_File_DB']
# COLECCION usuarios
collection = db['usuarios']
collection_accion = db['acciones']


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
                "contraseña": hashpass
                }
        post_id = collection.insert_one(post).inserted_id

        # Insertando acciones del sistema
        post = {"se_registro_usuario": name,
                "userID": post_id,
                "fecha_registro_usuario": datetime.today().strftime('%Y-%m-%d %I:%M %p'),
                "inicios_de_sesion": [],
                "creaste_asistentesVirt": [],
                "generaste_temas": [],
                "entrenaste_asistentesVirt": [],
                "iniaciaste_Server_Bot": []
                }
        post_id = collection_accion.insert_one(post).inserted_id

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
    # getpass es para no mostrar la contraseña al escribirla
    password = getpass.getpass('Entre su contraseña : ')
    login_user = collection.find_one({'nombre': name})

    if login_user and bcrypt.checkpw(
            password.encode('utf-8'), login_user['contraseña']):

        # Capturando la fecha y hora en que inicia sesion y la IP desde donde se inicia
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        # Actualizando acciones
        collection_accion.update_one(
            {'userID': login_user['_id']}, {
                '$push': {'inicios_de_sesion': {"userID": login_user["_id"], "fecha": datetime.today().strftime('%Y-%m-%d %I:%M %p'), "direc_IP": IPAddr}}}
        )
        print()
        os.system("cls")
        # Paso el id del usuario actual a todas las funciones
        cargaDatos.cargaDatos(login_user["_id"])

    else:
        print()
        print("ERROR de Usuario o contraseña" + '\n')
        opciones()


def opciones():

    os.system("cls")
    print("Bienvenido al Sistema de Generación de Conocimiento Automático para Asistentes Virtuales de Rasa")
    print()
    print()
    print("Recuerde que los datos entrados para la construcción del conocimiento una vez este dentro del sistema deben ser en Inglés. Los resultados serán dados en español.")
    print()
    print("- Si desea cancelar cualquier operación y salir a la pantalla principal del Sistema presione Ctrl + C" + "\n" + "- Si le sale al presionar Ctrl +C: " +
          "¿Desea terminar el trabajo por lotes (S/N)?, " + "presione s para cerrar o n para iniciar nuevamente el sistema")
    print()
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


opciones()
