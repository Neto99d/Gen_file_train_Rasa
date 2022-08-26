from pymongo import MongoClient
import questES
import subprocess
import entrenarAsistenteES
import createAVirtualES
import correrServerAsistente
import os


client = MongoClient()


# BASE DE DATOS
db = client['rasa_File_DB']
collection = db['contenido']


def cargaDatos(user):
   #################################################################
 print("OPCIONES" + "\n" "1. Crear Asistente Virtual" +
          "\n" "2. Generar Conocimiento" + "\n" + "3. Entrenar Asistente" + "\n"  "4. Probar Asistente" + "\n" "5. Correr servidor de un Asistente (Sólo para uso remoto, por ejemplo si está conectado a un Telegram-Bot)")
 try:
    no = input("Entre el número de la opción: ")
    if(no == '1'):
        os.system("cls")
        createAVirtualES.creaAsistente(user)
    elif(no == '2'):
        os.system("cls")
        questES.main(user)
    elif (no == '3'):
        os.system("cls")
        entrenarAsistenteES.entrenar(user)
    elif (no == '4'):
        os.system("cls")
        mostrarAsistentes(user)
    elif (no == '5'):
       os.system("cls")
       correrServerAsistente.mostrarAsistentes(user)
    else:
        print()
        print()
        print("Sólo los valores 1 al 5")
        cargaDatos(user)
 except Exception as error:
            print(error)
            os.system("cls")
            print("Error al iniciar opción deseada")
            print()
            cargaDatos(user)

def mostrarAsistentes(user):
    print()
    cont = 0
    entrenado = ""
    collection = db['bots_virtuales']

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
            print(str(result) + "." + " " + item['nombre'] + "      " + "Ha sido entrenado?: " + entrenado)
        print()
        probarAsistentes(user)
    else:
        print()
        print('Aún no tiene Asistentes creados.' + "\n")
        cargaDatos(user)


def probarAsistentes(user):
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
            if (asistente['entrenado']):
              print('Ha sido entrenado: ' + "Sí" )
              print()
            else:
              print('Ha sido entrenado: ' + "No" )
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
                    print("Estableciendo conversación de prueba......")
                    print()
                    print(
                        "Para terminar la conversación con el asistente envíele un mensaje que diga   /stop")
                    print()
                    os.system("rasa shell")
                    os.system("cls")
                    cargaDatos(user)
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
                print("Estableciendo conversación de prueba......")
                print()
                print(
                    "Para terminar la conversación con el asistente envíele un mensaje que diga   /stop")
                print()
                os.system("rasa shell")
                os.system("cls")
                cargaDatos(user)
            else:
                print()
                mostrarAsistentes(user)
        except Exception as error:
            print(error)
            print("Este asistente virtual no está entre los que tiene creados")
            print()
            mostrarAsistentes(user)
