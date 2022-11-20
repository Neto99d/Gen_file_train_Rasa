#import questES
import subprocess
import entrenarAsistenteES
import createAVirtualES
import correrServerAsistente
import genQuestBeta_esp_V1 as genQuesAnsw_v1
import genQuestBeta_esp_V2 as genQuesAnsw_v2
import genQuestBeta_esp_V3 as genQuesAnsw_v3
import os





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
            #questES.main(user) # En desuso (Solo usado en la rama develop_neto del proyecto)
            genQuesAnsw_v3.inicio(user) # Usando Modelos Pre-Entrenados para generar preguntas y respuestas
            #genQuesAnsw_v2.inicio(user) # Usando Entidades nombradas para generar preguntas y para respuestas un modelo pre-entrenado 
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



