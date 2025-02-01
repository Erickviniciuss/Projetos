import flet as ft


def main(pagina):
    tt = ft.Text('RSTZAP')
    pagina.update()


    def enviar_tunel(msg):
        texto = ft.Text(msg)
        chat.controls.append(texto)
        pagina.update()


    pagina.pubsub.subscribe(enviar_tunel)


    def enviar_msg_t(ev):
        nome_usuario = caixa_nome.value
        texto_campo = enviar_msg.value
        msg = f'{nome_usuario}: {texto_campo}'
        pagina.pubsub.send_all(msg)
        enviar_msg.value = ""
        pagina.update()


    chat_msg = ft.Text('Bem Vindo ao Chat!')
    enviar_msg = ft.TextField(label='Digite sua mensagem', on_submit=enviar_msg_t)
    botao_msg = ft.ElevatedButton('Enviar',on_click=enviar_msg_t)
    linha = ft.Row([enviar_msg, botao_msg])
    chat = ft.Column()


    def entrar_chat(ev):
        popup.open = False
        pagina.remove(tt)
        pagina.remove(botao)
        pagina.add(chat_msg)
        pagina.add(chat)
        pagina.add(linha)
        nome_usuario = caixa_nome.value
        msg = f'{nome_usuario} entrou no chat'
        pagina.pubsub.send_all(msg)
        pagina.update()


    popuptx = ft.Text('Bem Vindo ao RSTZAP')
    caixa_nome = ft.TextField(label='Digite seu nome')
    botao_popup = ft.ElevatedButton('Entrar no chat',on_click=entrar_chat)
    popup = ft.AlertDialog(title=popuptx, content=caixa_nome, actions=[botao_popup])


    def abrir_pop(ev):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    botao = ft.ElevatedButton('Iniciar Chat', on_click=abrir_pop)
    pagina.add(tt)
    pagina.add(botao)


ft.app(main, view=ft.WEB_BROWSER)
