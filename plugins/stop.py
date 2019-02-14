# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['stop'], 
    func=lambda m: 
        not utils.is_banned(m.chat.id)
    )
def command_stop(m):
    cid = m.chat.id
    if utils.is_user(cid):
        bot.send_sticker(cid, 'CAADAgAD-SYAAktqAwABJKWBkTWlpzoC')
        bot.send_message(cid, responses[utils.lang(cid)]['stop'])
        users.update_one({"_id": str(cid)}, {"$set": {"active": False}})
        for id in admins:
            bot.send_message(id, "Usuario eliminado:\n\nNombre: " +
                str(m.from_user.first_name) +
                "\nAlias: @" +
                str(m.from_user.username) +
                "\nID: " +
                str(cid))
    else:
        bot.send_message(cid, responses[utils.lang(cid)]['already_stopped'])
