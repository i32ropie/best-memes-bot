# -*- coding: utf-8 -*-

from config import *

def listener(messages):
    for m in messages:
        cid = m.chat.id
        uid = m.from_user.id
        if utils.is_admin(cid):
            if m.content_type == "photo":
                file_id = m.photo[-1].file_id
                if len(file_id) > 62:
                    bot.send_message(cid, responses[utils.lang(cid)]['file_id_long'])
                    return
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
                    bot.send_message(cid, responses[utils.lang(cid)]['stored'])
                else:
                    bot.send_message(cid, responses[utils.lang(cid)]['alredy_stored'])
        else:
            if m.content_type == "text":
                if cid > 0:
                    log_line = "<" + str(m.message_id) + "> " + time.strftime("%d %b %Y %H:%M:%S ", time.localtime()) + str(
                        m.from_user.first_name) + " (@" + str(m.from_user.username) + ") <- [" + str(cid) + "]: " + m.text + "\n"
                else:
                    log_line = "<" + str(m.message_id) + "> " + time.strftime("%d %b %Y %H:%M:%S ", time.localtime()) + str(
                        m.from_user.first_name) + " (@" + str(m.from_user.username) + ") <- [" + str(uid) + "][" + str(cid) + "]: " + m.text + "\n"
                if str(cid) in filtered:
                    for x in admins:
                        bot.send_message(x, log_line)
            if m.content_type == "photo":
                file_id = m.photo[-1].file_id
                if len(file_id) > 62:
                    bot.send_message(cid, responses[utils.lang(cid)]['file_id_long'])
                    message = f"😢 Meme recibido pero con file_id demasiado largo 😢\n\nID Meme: <code>{file_id}</code>\nIdioma: {utils.lang(cid)}\nFecha envío: {m.date}\nID mensaje: {m.message_id}\nID creador: <a href=\"tg://user?id={cid}\">{cid}</a>"
                    for x in admins:
                        bot.send_photo(x, file_id, caption=message, parse_mode="html")
                    return
                if not memes.find_one(file_id):
                    bot.send_message(cid, responses[utils.lang(cid)]['review'])
                    keyboard = types.InlineKeyboardMarkup()
                    accept = types.InlineKeyboardButton("✅", callback_data=f"A {file_id}")
                    decline = types.InlineKeyboardButton("❌", callback_data=f"R {file_id}")
                    keyboard.add(accept, decline)
                    message = f"🔔 Meme recibido 🔔\n\nID Meme: <code>{file_id}</code>\nIdioma: {utils.lang(cid)}\nFecha envío: {m.date}\nID mensaje: {m.message_id}\nID creador: <a href=\"tg://user?id={cid}\">{cid}</a>"
                    for x in admins:
                        bot.send_photo(x, file_id, caption=message, parse_mode="html", reply_markup=keyboard)
                else:
                    bot.send_message(cid, responses[utils.lang(cid)]['alredy_stored'])


bot.set_update_listener(listener)


@bot.callback_query_handler(func=lambda call: call.data.startswith('A '))
def callback_accept(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    meme = call.data.split()[1]
    m_text = call.message.caption.split('\n')
    date = m_text[4].split(': ')[1]
    m_id = m_text[5].split(': ')[1]
    c_id = m_text[6].split(': ')[1]
    memes.insert_one({
        "_id": meme,
        "categories": [],
        "register": int(date),
        "views": 0,
        "saves": 0,
        "uploader": str(c_id),
        "reviewer": str(cid)
    })
    try:
        bot.send_message(c_id, responses[utils.lang(c_id)]['accepted'], reply_to_message_id=m_id)
    except:
        pass
    message = f"✅ Meme guardado ✅\n\nID Meme: <code>{meme}</code>\nIdioma: {utils.lang(c_id)}\nFecha envío: {date}\nID mensaje: {m_id}\nID creador: <a href=\"tg://user?id={c_id}\">{c_id}</a>"
    bot.edit_message_caption(message, cid, mid, parse_mode="html")


@bot.callback_query_handler(func=lambda call: call.data.startswith('R '))
def callback_reject(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    meme = call.data.split()[1]
    m_text = call.message.caption.split('\n')
    date = m_text[4].split(': ')[1]
    m_id = m_text[5].split(': ')[1]
    c_id = m_text[6].split(': ')[1]
    try:
        bot.send_message(c_id, responses[utils.lang(c_id)]['rejected'], reply_to_message_id=m_id)
    except:
        pass
    message = f"❌ Meme rechazado ❌\n\nID Meme: <code>{meme}</code>\nIdioma: {utils.lang(c_id)}\nFecha envío: {date}\nID mensaje: {m_id}\nID creador: <a href=\"tg://user?id={c_id}\">{c_id}</a>"
    bot.edit_message_caption(message, cid, mid, parse_mode="html")