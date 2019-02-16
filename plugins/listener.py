# -*- coding: utf-8 -*-

from config import *

def listener(messages):
    for m in messages:
        cid = m.chat.id
        uid = m.from_user.id
        if utils.is_admin(cid):
            if m.content_type == "photo":
                file_id = m.photo[-1].file_id
                if not memes.find_one(file_id):
                    memes.insert_one({
                        "_id": file_id,
                        "categories": [],
                        "register": m.date,
                        "views": 0,
                        "saves": 0,
                        "uploader": str(uid),
                        "reviewer": str(uid)
                    })
                    bot.send_message(cid, "Meme guardado correctamente")
                else:
                    bot.send_message(cid, "Ese meme ya está guardado en la bd")

bot.set_update_listener(listener)