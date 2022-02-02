'''def chatlogs_html(messages):
    messages_html = "".join(["<p>{}</p>". format(m) for m in messages])
    chatbot_html = """< div class = "chat_window" {} < /div >""".Format(
        messages_html)
    return chatbot_html


while True:
    clear_output()
    display(IPython.display.HTML(chatlogs_html(messages)))
    time. sleep(0.3)
    respuesta = use()
    # print (str, respuestas)
    print(respuesta[0])
   # a = input('Hazme una pregunta: ')  #llamr funcion que recivbe un correo
    messages.append(respuesta[0])  # print (messages)
    if respuesta == 'stop':
        break
        # print (responses [ "text"))
        responses = agent.handle_message(respuesta[0])
    # enviar (responses [ "text")).
    for r in responses:
        messages.append(r.get("text"))
        print(r.get("text"))
        enviar(r.get("text"), respuesta[1])'''
