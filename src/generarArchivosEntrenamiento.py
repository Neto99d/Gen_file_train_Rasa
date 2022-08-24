import fileNLU
import fileDomain
import fileStories
import fileRules
import os


def generarArchivos(preguntas, respuestas):
    if (fileDomain.domYaml(preguntas, respuestas) &
            fileNLU.nluYaml(preguntas, respuestas) &
            fileStories.storiesYaml(preguntas, respuestas) &
            fileRules.rulesYaml(preguntas, respuestas)):
        os.system("cls")
        print(
            '\n' + "Archivos de entrenamiento creados con Exito :)" + '\n' '..............................')
        print()
    
    else:
        print()
        print("Algo salio mal al generar archivos :( ")
