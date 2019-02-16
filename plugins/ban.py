# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['ban'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_ban(m):
    cid = m.chat.id
    if len(m.text.split()) == 1:
        bot.send_message(cid, "Error. Debes introducir el ID del usuario a banear.")
        return
    ids_to_ban = m.text.split()[1:]
    for x in ids_to_ban:
        if utils.is_user(x):
            users.update_one(
                {
                    "_id": x
                },
                {
                    "$set" : {
                        "banned" : True
                    }
                }
            )
        else:
            users.insert_one({
                "_id": x,
                "lang": "en",
                "active": False,
                "banned": True,
                "register": m.date,
                "notify": False,
                "returns": [],
                "memes": [],
                "saved": []
            })
    bot.send_message(cid, "Baneo exitoso.")


@bot.message_handler(
    commands=['unban'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_unban(m):
    cid = m.chat.id
    if len(m.text.split()) == 1:
        bot.send_message(cid, "Error. Debes introducir el ID del usuario a desbanear.")
        return
    ids_to_unban = m.text.split()[1:]
    count = 0
    for x in ids_to_unban:
        if utils.is_user(x):
            count += 1
            users.update_one(
                {
                    "_id": x
                },
                {
                    "$set" : {
                        "banned" : False
                    }
                }
            )
    if count != 0:
        bot.send_message(cid, "Desbaneo exitoso.")
    else:
        bot.send_message(cid, "Error. Debes introducir un usuario existente.")
