import os
dirname, filename = os.path.split(os.path.abspath(__file__))


def iniciarWebChat():
    print()
    print("Iniciando Web Chat...... La página se abrirá automáticamente en su navegador")
    print()
    # Donde esta la pagina web de Chat
    os.chdir(dirname + os.path.sep + "WebChat")
    # Iniciar un servidor web con python
    os.system("start http://[::1]:8080/")
    os.system("python -m http.server --bind localhost 8080")
    
    
iniciarWebChat()    