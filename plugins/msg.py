# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['msg'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_msg(m):
    cid = m.chat.id
    if len(m.text.split()) < 3:
        bot.send_message(cid, "Error. Debes introducir `/msg <ID> [!] <Mensaje>` | Empieza el mensaje con *!* para usar Markdown", parse_mode="Markdown")
        return
    c_id = m.text.split(None,2)[1]
    answer = m.text.split(None, 2)[3]
    parse_mode = "Markdown" if answer.startswith('!') else None
    try:
        bot.send_message(
            c_id,
            answer.lstrip('!'),
            parse_mode=parse_mode)
    except Exception as e:
        bot.send_message(
            52033876,
            utils.send_exception(e),
            parse_mode="Markdown")