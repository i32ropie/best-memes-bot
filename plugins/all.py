# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    func=lambda m: 
        utils.is_admin(m.from_user.id) and
        m.text and m.text.startswith('/all')
    )
def command_CMD(m):
    cid = m.chat.id
    save = list()
    delete = list()
    if len(m.text.split()) == 1:
        bot.send_message(cid, "Error. No has escrito ningún texto para difundir.")
        return
    group = m.text.split()[0].split('_')[1] if len(m.text.split()[0].split('_')) == 2 else None
    if group and group not in responses.keys():
        bot.send_message(cid, f"Error. El idioma '*{group}*' no existe aún en el bot.", parse_mode="Markdown")
        return
    if group and group in responses.keys():
        for x in [y['_id'] for y in users.find({"banned": False, "active": True, "lang": group})]:
            try:
                bot.send_message(x, m.text.split(None, 1)[1])
            except Exception as e:
                try:
                    if e.result.status_code == 403:
                        delete.append(x)
                        users.update({"_id": x}, {"$set": {"active": False}})
                except Exception as z:
                    bot.send_message(
                        52033876, utils.send_exception(e), parse_mode="Markdown")
                    bot.send_message(
                        52033876, utils.send_exception(z), parse_mode="Markdown")
            else:
                save.append(x)
    if not group:
        for x in [y['_id'] for y in users.find({"banned": False, "active": True})]:
            try:
                bot.send_message(x, m.text.split(None, 1)[1])
            except Exception as e:
                try:
                    if e.result.status_code == 403:
                        delete.append(x)
                        users.update({"_id": x}, {"$set": {"active": False}})
                except Exception as z:
                    bot.send_message(
                        52033876, utils.send_exception(e), parse_mode="Markdown")
                    bot.send_message(
                        52033876, utils.send_exception(z), parse_mode="Markdown")
            else:
                save.append(x)
    bot.send_message(cid, f"Conservados: {len(save)}\nEliminados: {len(delete)}")

