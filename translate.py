

from deep_translator import GoogleTranslator

# - - Esta parte del código traduce únicamente un texto plano
traductor = GoogleTranslator(source='auto', target='es')
resultado = traductor.translate("Education is the most powerful weapon to change the world")
print(resultado)
#-----------------------------------------------------------------------------


# - - Esta parte del código traduce un archivo, esta comentada porque si el archivo no existe dará error.
#translated = GoogleTranslator(source='en', target='es').translate_file(r'C:\Users\Tecsify.txt')
#print(translated)
#-----------------------------------------------------------------------------


# - - Esta parte del código traduce una lista de palabras por separado sin que se vean afectadas por el contexto de la oración
lista = ["Tecsify","¡Tecnología","que","Empodera!"]
traductor = GoogleTranslator(source='auto', target='es')
resultado = traductor.translate_batch(lista)
print(resultado)
#-----------------------------------------------------------------------------