from pymongo import MongoClient
import subprocess
import os
from datetime import datetime
import cargaDatos

client = MongoClient()


# BASE DE DATOS
db = client['rasa_File_DB']
dirname, filename = os.path.split(os.path.abspath(__file__))
collection_accion = db['acciones']

def mostrarAsistentes(user):
    print("- Si desea cancelar cualquier operación y salir a la pantalla principal del Sistema presione Ctrl + C" + "\n" + "- Si le sale al presionar Ctrl +C: " +
          "¿Desea terminar el trabajo por lotes (S/N)?, " + "presione s para cerrar o n para iniciar nuevamente el sistema")
    print()
    cont = 0
    collection = db['asistentes_virtuales']
    entrenado = ""
    asistentes = collection.find_one(
        {'creado_por': user})  # Comprobar que el usuario corresponde al usuario actual, si no se corresponde se genera una excepcion o error
    print()
    if(asistentes):  # Si existen
        print('Lista de sus Asistentes Virtuales')
        for item in collection.find({'creado_por': user}):
            result = cont = cont + 1
            if (item['entrenado']):
                entrenado = "Sí"
            else:
                entrenado = "No"
            print(str(result) + "." + " " +
                  item['nombre'] + "      " + "Ha sido entrenado?: " + entrenado)
        print()
        cargarAsistentes(user)
    else:
        print()
        print('Aún no tiene Asistentes creados.' + "\n")
        cargaDatos.cargaDatos(user)


def cargarAsistentes(user):
    print()
    collection = db['asistentes_virtuales']
    nombre_asistente = input(
        "Escriba el nombre del asistente que desee probar: ")
    if (nombre_asistente):
        try:
            asistente = collection.find_one(
                {'nombre': nombre_asistente, 'creado_por': user})  # Comprobar que el usuario corresponde al usuario actual, si no se corresponde se genera una excepcion o error
            print()
            print('Vista de los datos correspondientes al asistente elegido')
            print()
            print('Nombre: ' +
                  str(asistente['nombre']))
            print()
            print('Descripción: ' + str(asistente['descripcion']))
            print()
            print('Alojado en: ' + str(asistente['alojado_en']))
            print()
            if (asistente['entrenado']):
                print('Ha sido entrenado: ' + "Sí")
                print()
            else:
                print('Ha sido entrenado: ' + "No")
                print()
            print('Se creó en la fecha: ' + str(asistente['fecha_creado']))
            print()
            confirmar = input(
                "Confirme que este es el que desea cargar: Escriba si o no: ")
            if (confirmar == 'si'):
                print()
                print("El directorio o carpeta dónde está su Asistente Virtual es: ", str(
                    asistente['alojado_en']))
                confirmarDir = input(
                    "Confirme que este es el directorio o carpeta actual: Escriba si o no: ")
                if (confirmarDir == 'si'):
                    print()
                    os.system("cls")
                    os.chdir(str(asistente['alojado_en']))
                    print("Iniciando servidor Rasa......")
                    print()
                    print()
                    print(
                        "Una vez que el servidor este corriendo puede ejecutar el archivo  IniciarWebChat.bat  para interactuar con el Asistente Virtual")
                    print()
                    print(
                        "Cuando vea que pone este mensaje <<< root  - Rasa server is up and running. >>> Es que ya el servidor está corriendo")
                    print()
                    # Actualizando acciones
                    collection_accion.update_one(
                        {'userID': user}, {
                            '$push': {"iniaciaste_Server_Bot": {"nombre_asistente": asistente['nombre'], "asistenteID": asistente['_id'], "fecha_inicio_Bot": datetime.today().strftime('%Y-%m-%d %I:%M %p')}}}
                    )
                    # para que rasa escuche desde el servidor web
                    os.system("rasa run --cors *")
                else:
                    print()
                    print("Entre la dirección del directorio o carpeta actual donde está el Asistente (Está información se actualizará en la base de datos) y luego presione ENTER")
                dir = input()
                os.chdir(dir)
                collection.update_one(
                    {'nombre': nombre_asistente, 'creado_por': user}, {
                        '$set': {'alojado_en': os.getcwd()}}
                )
                os.system("cls")
                os.chdir(str(asistente['alojado_en']))
                print("Iniciando servidor Rasa......")
                print()
                print(
                    "Una vez que el servidor este corriendo puede ejecutar el archivo  IniciarWebChat.bat  para interactuar con el Asistente Virtual")
                print()
                print("Cuando vea que pone este mensaje <<< root  - Rasa server is up and running. >>> Es que ya el servidor está corriendo")
                print()
                # Actualizando acciones
                collection_accion.update_one(
                    {'userID': user}, {
                        '$push': {"iniaciaste_Server_Bot": {"nombre_asistente": asistente['nombre'], "asistenteID": asistente['_id'], "fecha_inicio_Bot": datetime.today().strftime('%Y-%m-%d %I:%M %p')}}}
                )
                os.system("rasa run --cors *")

            else:
                print()
                mostrarAsistentes(user)
        except Exception as error:
            print()
            print("Este asistente virtual no está entre los que tiene creados")
            print()
            mostrarAsistentes(user)
