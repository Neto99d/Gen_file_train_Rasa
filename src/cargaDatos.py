from pymongo import MongoClient
# import quest
import questES


client = MongoClient()


# BASE DE DATOS
db = client['rasa_File_DB']
collection = db['contenido']


def cargaDatos(user):
   #################################################################
    print("OPCIONES" + "\n" "1. Nuevo" +
          "\n" "2. Cargar desde datos guardados" + "\n")

    no = input("Entre el número de la opción: ")
    cont = 0
    if(no == '1'):
        questES.main(user)
    elif(no == '2'):
        collectionUser = db['users']
        userFind = collectionUser.find_one({'nombre': user})
        datosFind = collection.find_one({'user': user})
        if(userFind and datosFind): # Si existen
            print('Datos guardados, se muestran por Asunto del contenido.')
            for item in collection.find({'user': user}): # Listar los asuntos segun el usuario logueado
                result = cont = cont + 1
                print(str(result) + "." + " " + item['asunto'])
            print()
            cargarAsunto(user)
        else:
            print()
            print('Aún no tiene datos guardados.' + "\n")
            cargaDatos(user)
    else:
        print()
        print()
        print("Sólo los valores 1 o 2")
        cargaDatos(user)


def cargarAsunto(user):
    print()
    nombre_asunto = input(
        "Escriba el asunto que desee cargar: ")
    if (nombre_asunto):
        try:
            asunto = collection.find_one(
                {'asunto': nombre_asunto, 'user': user}) # Comprobar que el asunto entrado corresponde al usuario actual, si no se corresponde se genera una excepcion o error 
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
                questES.mainCargaDatos(
                    asunto['questions'], asunto['responses'])
            else:
                cargarAsunto(user)
        except Exception as error:
            print()
            print("Este asunto no está entre sus datos guardados")
            print()
            cargarAsunto(user)
