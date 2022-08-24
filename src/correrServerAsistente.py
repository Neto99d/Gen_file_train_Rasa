from pymongo import MongoClient
import subprocess
import os


client = MongoClient()


# BASE DE DATOS
db = client['rasa_File_DB']


def mostrarAsistentes(user):
    print("- Si desea cancelar cualquier operación y salir a la pantalla principal del Sistema presione Ctrl + C" + "\n" + "- Si le sale al presionar Ctrl +C: " +
          "¿Desea terminar el trabajo por lotes (S/N)?, " + "presione s para cerrar o n para iniciar nuevamente el sistema")
    print()
    cont = 0
    collection = db['bots_virtuales']

    asistentes = collection.find_one(
        {'creado_por': user})  # Comprobar que el usuario corresponde al usuario actual, si no se corresponde se genera una excepcion o error
    print()
    if(asistentes):  # Si existen
        print('Lista de sus Asistentes Virtuales')
        for item in collection.find({'creado_por': user}):
            result = cont = cont + 1
            print(str(result) + "." + " " + item['nombre'])
        print()
        cargarAsistentes(user)
    else:
        print()
        print('Aún no tiene Asistentes creados.' + "\n")
        cargaDatos(user)


def cargarAsistentes(user):
    print()
    collection = db['bots_virtuales']
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
                    print("Iniciando servidor......")
                    print()
                    os.system("rasa run")
                else:
                    print("Entre la dirección del directorio o carpeta actual donde está el Asistente (Está información se actualizará en la base de datos) y luego presione ENTER")
                dir = input()
                os.chdir(dir)
                collection.update_one(
                    {'nombre': nombre_asistente, 'creado_por': user}, {
                        '$push': {'alojado_en': dir}}
                )
                os.system("cls")
                print("Iniciando servidor......")
                print()
                os.system("rasa run")
            else:
                print()
                mostrarAsistentes(user)
        except Exception as error:
            print()
            print("Este asistente virtual no está entre los que tiene creados")
            print()
            mostrarAsistentes(user)
