import fileNLU
import fileDomain
import fileStories
import fileRules


def generarArchivos(preguntas, respuestas):
    if (fileDomain.domYaml(preguntas, respuestas) &
            fileNLU.nluYaml(preguntas, respuestas) &
            fileStories.storiesYaml(preguntas, respuestas) &
            fileRules.rulesYaml(preguntas, respuestas)):
        print(
            '\n' + "Creados con Exito :), en la carpeta Archivos_generados" + '\n' '..............................')
        print()
    
    else:
        print()
        print("Algo salio mal :( ")
