import shutil
import os
import generarArchivosEntrenamiento
from pymongo import MongoClient
import subprocess
import cargaDatos

client = MongoClient()


# BASE DE DATOS
db = client['rasa_File_DB']
collection = db['contenido']


def mover(dir):
    try:
        print()
        dirname, filename = os.path.split(os.path.abspath(__file__))
        #######################################
        print()
        print("Moviendo Archivos..........." + '\n')

        shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "domain.yml",
                    os.path.join(dir, "domain.yml"))
        shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "nlu.yml",
                    os.path.join(dir + "\data", "nlu.yml"))
        shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "stories.yml",
                    os.path.join(dir + "\data", "stories.yml"))
        shutil.move(dirname + os.path.sep + "Archivos_generados" + os.path.sep + "rules.yml",
                    os.path.join(dir + "\data", "rules.yml"))
        print("Archivos movidos a la carpeta del Asistente para ser entrenado" + '\n')
        return True

    except Exception as error:
        print(error)
        print("Error: No existe uno de los archivos de entrenamiento, o ninguno")
        print("Ejecute la herramienta nuevamente")
        return False


def entrenar(user):
    print()
    print("Ahora entrenaremos al Asistente")
    print()
    mostrarAsuntos(user)


#########################################

def mostrarAsuntos(user):
    collectionUser = db['users']
    userFind = collectionUser.find_one({'nombre': user})
    datosFind = collection.find_one({'user': user})
    cont = 0
    if(userFind and datosFind):  # Si existen
        print(
            'Contenidos guardados para entrenamiento, se muestran por Asunto del contenido.')
        # Listar los asuntos segun el usuario logueado
        for item in collection.find({'user': user}):
            result = cont = cont + 1
            print(str(result) + "." + " " + item['asunto'])
        print()
        cargarAsunto(user)
    else:
        print()
        print('Aún no tiene datos guardados.' + "\n")
        cargaDatos(user)


def cargarAsunto(user):
    print()
    nombre_asunto = input(
        "Escriba el asunto que desee cargar para entrenar el asistente: ")
    if (nombre_asunto):
        try:
            asunto = collection.find_one(
                {'asunto': nombre_asunto, 'user': user})  # Comprobar que el asunto entrado corresponde al usuario actual, si no se corresponde se genera una excepcion o error
            print()
            print('Vista de los datos correspondientes al asunto elegido')
            print()
            print('Texto: ' +
                  str(asunto['texto']))
            print()
            print('Preguntas: ' + str(asunto['questions']))
            print()
            print('Respuestas: ' + str(asunto['responses']))
            print()
            confirmar = input(
                "Confirme que este es el que desea cargar: Escriba si o no: ")
            if (confirmar == 'si'):
                print()
                generarArchivosEntrenamiento.generarArchivos(
                    asunto['questions'], asunto['responses'])
                mostrarAsistentes(user)
            else:
                print()
                os.system("cls")
                mostrarAsuntos(user)
        except Exception as error:
            print()
            print("Este asunto no está entre sus datos guardados")
            print()
            mostrarAsuntos(user)


def mostrarAsistentes(user):
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
        "Escriba el nombre del asistente que desee entrenar: ")
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
                    visualConocimiento = "rasa visualize"
                    train = "rasa train"
                    if mover(str(
                            asistente['alojado_en'])):
                        print("Entrenando al Asistente")
                        print("Espere......... Esta cargando....")
                        os.chdir(str(
                            asistente['alojado_en']))
                        os.system(train)
                        print()
                        os.system("cls")
                        print("Se le mostrará un gráfico en su navegador donde podrá ver las preguntas y las respuestas inferidas a cada pregunta (utter_pregunta) después del entrenamiento, para verificar que el Asistente tendrá alta probabilidad de responder correctamente.")
                        print()
                        print("Cargando............")
                        os.system(visualConocimiento)
                        print()
                        cargaDatos.cargaDatos(user)
                else:
                    print("Entre la dirección del directorio o carpeta actual donde está el Asistente (Está información se actualizará en la base de datos) y luego presione ENTER")
                    dir = input()
                    os.chdir(dir)
                    collection.update_one(
                        {'nombre': nombre_asistente, 'creado_por': user}, {
                            '$push': {'alojado_en': dir}}
                    )
                    if mover(dir):
                        visualConocimiento = "rasa visualize"
                        train = "rasa train"
                        print("Entrenando al Asistente")
                        print("Espere......... Esta cargando....")
                        os.chdir(dir)
                        os.system(train)
                        print()
                        os.system("cls")
                        print("Se le mostrará un gráfico en su navegador donde podrá ver las preguntas y las respuestas inferidas a cada pregunta (utter_pregunta) después del entrenamiento, para verificar que el Asistente tendrá alta probabilidad de responder correctamente.")
                        print()
                        print("Cargando............")
                        os.system(visualConocimiento)
                        print()
                        cargaDatos.cargaDatos(user)
            else:
                print()
                mostrarAsistentes(user)
        except Exception as error:
            print(error)
            print("Este asistente virtual no está entre los que tiene creados")
            print()
            mostrarAsistentes(user)
