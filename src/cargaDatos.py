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
          "\n" "2. Generar Conocimiento" + "\n" + "3. Entrenar Asistente" + "\n"  "4. Probar Asistente" + "\n")
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
            correrServerAsistente.mostrarAsistentes(user)
        else:
            print()
            print()
            print("Sólo los valores 1 al 4")
            cargaDatos(user)
    except Exception as error:
        os.system("cls")
        print(error)
        print("Error al iniciar opción deseada")
        print()
        cargaDatos(user)



