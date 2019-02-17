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
                "saved": [],
                "reported": []
            })
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(responses[utils.lang(cid)]['start_message'], callback_data='start'))
        bot.send_message(cid, responses[utils.lang(cid)]['start'], parse_mode="Markdown", reply_markup=keyboard)
        for id in admins:
            bot.send_message(id, "Nuevo usuario\n\nNombre: " +
                                 str(m.from_user.first_name) +
                                 "\nAlias: @" +
                                 str(m.from_user.username) +
                                 "\nID: " +
                                 str(cid) +
                                 "\nIdioma: " +
                                 str(ulang))
    else:
        bot.send_message(cid, responses[utils.lang(cid)]['already_started'])


@bot.callback_query_handler(func=lambda call: call.data == 'start')
def callback_start(call):
    cid = call.message.chat.id
    # mid = call.message.message_id
    keyboard = types.InlineKeyboardMarkup()
    chat_memes = users.find_one(str(cid))['memes']
    prev_meme = chat_memes[-1] if chat_memes else None
    next_button = types.InlineKeyboardButton('->', callback_data='newmeme')
    if prev_meme:
        prev_button = types.InlineKeyboardButton('<-', callback_data=f'm {prev_meme}')
        keyboard.add(prev_button, next_button)
    else:
        keyboard.add(next_button)
    meme = utils.random_meme(cid)
    if meme:
        save_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['save_meme'], callback_data=f's {meme}')
        keyboard.add(save_button)
        report_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['report_meme'], callback_data=f'r {meme}')
        keyboard.add(report_button)
        bot.send_photo(cid, meme, caption=f'<code>{meme}</code>', reply_markup=keyboard, parse_mode='html')
    else:
        bot.send_message(cid, responses[utils.lang(cid)]['no_more'])