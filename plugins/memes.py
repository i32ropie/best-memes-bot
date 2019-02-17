# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['memes'],
    func=lambda m: 
        utils.is_recent(m) and 
        utils.is_user(m.chat.id) and 
        not utils.is_banned(m.chat.id)
    )
def command_memes(m):
    cid = m.chat.id
    keyboard = types.InlineKeyboardMarkup()
    chat_memes = users.find_one(str(cid))['memes']
    prev_meme = chat_memes[-1] if chat_memes else None
    if len(chat_memes) != memes.find().count():
        next_button = types.InlineKeyboardButton('➡️', callback_data='newmeme')
    else:
        next_button = None
        prev_meme = chat_memes[-2]
    if prev_meme:
        prev_button = types.InlineKeyboardButton('⬅️', callback_data=f'm {prev_meme}')
    else:
        prev_button = None
    if next_button and prev_button:
        keyboard.add(prev_button, next_button)
    if next_button and not prev_button:
        keyboard.add(next_button)
    if not next_button and prev_button:
        keyboard.add(prev_button)
    meme = utils.random_meme(cid)
    if meme:
        save_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['save_meme'], callback_data=f's {meme}')
        keyboard.add(save_button)
        report_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['report_meme'], callback_data=f'r {meme}')
        keyboard.add(report_button)
        bot.send_photo(cid, meme, reply_markup=keyboard, parse_mode='html')
    else:
        meme = chat_memes[-1]
        save_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['save_meme'], callback_data=f's {meme}')
        keyboard.add(save_button)
        report_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['report_meme'], callback_data=f'r {meme}')
        keyboard.add(report_button)
        bot.send_photo(cid, meme, reply_markup=keyboard, parse_mode='html')


@bot.callback_query_handler(func=lambda call: call.data == 'newmeme')
def callback_newmeme(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    keyboard = types.InlineKeyboardMarkup()
    meme = utils.random_meme(cid)
    chat_memes = users.find_one(str(cid))['memes']
    prev_meme = chat_memes[-2] if chat_memes else None
    prev_button = types.InlineKeyboardButton('⬅️', callback_data=f'm {prev_meme}')
    if len(chat_memes) != memes.find().count():
        next_button = types.InlineKeyboardButton('➡️', callback_data='newmeme')
        keyboard.add(prev_button, next_button)
    else:
        keyboard.add(prev_button)
    save_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['save_meme'], callback_data=f's {meme}')
    keyboard.add(save_button)
    report_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['report_meme'], callback_data=f'r {meme}')
    keyboard.add(report_button)
    bot.edit_message_media(types.InputMediaPhoto(meme, parse_mode='html'), cid, mid, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('m '))
def callback_meme(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    meme = call.data.split()[1]
    keyboard = types.InlineKeyboardMarkup()
    chat_memes = users.find_one(str(cid))['memes']
    try:
        prev_meme = chat_memes[chat_memes.index(meme) - 1] if meme != chat_memes[0] else None
    except:
        prev_meme = None
    try:
        next_meme = chat_memes[chat_memes.index(meme) + 1]
    except:
        next_meme = None
    if next_meme:
        next_button = types.InlineKeyboardButton('➡️', callback_data=f'm {next_meme}')
    else:
        if len(chat_memes) != memes.find().count():
            next_button = types.InlineKeyboardButton('➡️', callback_data='newmeme')
        else:
            next_button = None
    if prev_meme:
        prev_button = types.InlineKeyboardButton('⬅️', callback_data=f'm {prev_meme}')
    if next_button and prev_button:
        keyboard.add(prev_button, next_button)
    if next_button and not prev_button:
        keyboard.add(next_button)
    if not next_button and prev_button:
        keyboard.add(prev_button)  
    save_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['save_meme'], callback_data=f's {meme}')
    keyboard.add(save_button)
    report_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['report_meme'], callback_data=f'r {meme}')
    keyboard.add(report_button)
    bot.edit_message_media(types.InputMediaPhoto(meme, parse_mode='html'), cid, mid, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('s '))
def callback_save(call):
    cid = call.message.chat.id
    saved_memes = users.find_one(str(cid))['saved']
    meme = call.data.split()[1]
    if meme not in saved_memes:
        bot.answer_callback_query(call.id, responses[utils.lang(cid)]['meme_saved'])
        users.update_one(
            {
                '_id': str(cid)
            },
            {
                '$push': {
                    'saved': meme
                }
            }
        )
        memes.update_one(
            {
                '_id': meme
            },
            {
                '$inc': {
                    'saves': 1
                }
            }
        )
    else:
        bot.answer_callback_query(call.id, responses[utils.lang(cid)]['already_saved'])


@bot.callback_query_handler(func=lambda call: call.data.startswith('u '))
def callback_unsave(call):
    cid = call.message.chat.id
    saved_memes = users.find_one(str(cid))['saved']
    meme = call.data.split()[1]
    if meme in saved_memes:
        bot.answer_callback_query(call.id, responses[utils.lang(cid)]['meme_unsaved'])
        users.update_one(
            {
                '_id': str(cid)
            },
            {
                '$pull': {
                    'saved': meme
                }
            }
        )
        memes.update_one(
            {
                '_id': meme
            },
            {
                '$inc': {
                    'saves': -1
                }
            }
        )
    else:
        bot.answer_callback_query(call.id, responses[utils.lang(cid)]['already_unsaved'])


@bot.callback_query_handler(func=lambda call: call.data.startswith('r '))
def callback_report(call):
    cid = call.message.chat.id
    reported_memes = users.find_one(str(cid))['reported']
    meme = call.data.split()[1]
    if meme not in reported_memes:
        bot.answer_callback_query(call.id, responses[utils.lang(cid)]['meme_reported'])
        users.update_one(
            {
                '_id': str(cid)
            },
            {
                '$push': {
                    'reported': meme
                }
            }
        )
        meme_info = memes.find_one(meme)
        message = f"❌ Meme reportado ❌\n\nID Meme: <code>{meme}</code>\nMeme revisado por: <a href=\"tg://user?id={meme_info['reviewer']}\">{meme_info['reviewer']}</a>\nIdioma: {utils.lang(cid)}\nID mensaje: {call.message.message_id}\nID reportador: <a href=\"tg://user?id={cid}\">{cid}</a>"
        for x in admins:
            bot.send_photo(x, meme, caption=message, parse_mode="html")
    else:
        bot.answer_callback_query(call.id, responses[utils.lang(cid)]['already_reported'])
