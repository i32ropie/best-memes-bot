# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['admin'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_admin(m):
    cid = m.chat.id
    txt = """
Comandos de administración

/github - Comprueba si hay actualizaciones en github y reinicia el bot sin es necesario.
/all _<mensaje>_ - Difundido a todos los usuarios.
/all\_<idoma> _<mensaje>_ - Difundido al idioma pasado.
/ban _<id>_ - Banea un ID.
/unban _<id>_ - Desbanea un ID.
/exec _<code>_ - Ejecuta el siguiente bloque de código.
/res _[!]_ _<mensaje>_- Usado respondiendo a un mensaje de contacto le responde. Empieza la respuesta por ! para usar Markdown.
/msg _<id>_ _[!]_ _<mensaje>_ - Envia un mensaje a un ID.
/reload - Reiniciar el bot.   
"""
    bot.send_message(cid, txt, parse_mode="Markdown")