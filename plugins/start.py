# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['start'], 
    func=lambda m: 
        not utils.is_banned(m.chat.id)
    )
def command_start(m):
    cid = m.chat.id
    date = m.date
    ulang = m.from_user.language_code[:2] if m.from_user.language_code and m.from_user.language_code[:2] in ['en', 'es'] else 'en'
    if not utils.is_user(cid):
        if utils.was_user(cid):
            users.update({"_id": str(cid)}, {"$set": {"active": True}})
            users.update({"_id": str(cid)}, {"$push": {"returns": date}})
            users.update({"_id": str(cid)}, {"$set": {"lang": ulang}})
            users.update({"_id": str(cid)}, {"$set": {"notify": True}})
        else:
            users.insert_one({
                "_id": str(cid),
                "lang": ulang,
                "active": True,
                "banned": False,
                "register": date,
                "notify": True,
                "returns": [],
                "memes": [],
                "saved": []
            })
        bot.send_message(cid, responses[utils.lang(cid)]['start'])
        for id in admins:
            bot.send_message(id, f"Nuevo usuario: [{cid}](tg://user?id={cid})", parse_mode="Markdown")
    else:
        bot.send_message(cid, responses[utils.lang(cid)]['already_started'])
