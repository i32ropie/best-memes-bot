# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['filter'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_filter(m):
    cid = m.chat.id
    if len(m.text.split()) != 2:
        bot.send_message(cid, "Error. Debes pasar un ID para filtrar el chat.")
        return
    c_id = m.text.split(None, 1)[1]
    if c_id not in filtered:
        filtered.append(c_id)
        bot.send_message(cid, "El chat {} será redirigido.".format(c_id))
    elif c_id in filtered:
        filtered.remove(c_id)
        bot.send_message(
            cid, "El chat {} dejará de ser redirigido.".format(c_id))