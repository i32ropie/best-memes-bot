# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['saved'],
    func=lambda m: 
        utils.is_recent(m) and 
        utils.is_user(m.chat.id) and 
        not utils.is_banned(m.chat.id)
    )
def command_saved(m):
    cid = m.chat.id
    keyboard = types.InlineKeyboardMarkup()
    saved_memes = users.find_one(str(cid))['saved']
    if not saved_memes:
        bot.send_message(cid, responses[utils.lang(cid)]['no_saved'])
        return
    if len(saved_memes) > 1:
        next_meme = saved_memes[1]
    else:
        next_meme = None
    if next_meme:
        next_button = types.InlineKeyboardButton('->', callback_data=f'Saved {next_meme}')
        keyboard.add(next_button)
    meme = saved_memes[0]
    save_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['delete_meme'], callback_data=f'save {meme}')
    keyboard.add(save_button)
    bot.send_photo(cid, meme, caption=f'<code>{meme}</code>', reply_markup=keyboard, parse_mode='html')


@bot.callback_query_handler(func=lambda call: call.data.startswith('Saved'))
def callback_meme(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    meme = call.data.split()[1]
    keyboard = types.InlineKeyboardMarkup()
    saved_memes = users.find_one(str(cid))['saved']
    try:
        prev_meme = saved_memes[saved_memes.index(meme) - 1] if meme != saved_memes[0] else None
    except:
        prev_meme = None
    try:
        next_meme = saved_memes[saved_memes.index(meme) + 1]
    except:
        next_meme = None
    if next_meme:
        next_button = types.InlineKeyboardButton('->', callback_data=f'Saved {next_meme}')
    if prev_meme:
        prev_button = types.InlineKeyboardButton('<-', callback_data=f'Saved {prev_meme}')
    if next_meme and prev_meme:
        keyboard.add(prev_button, next_button)
    if next_meme and not prev_meme:
        keyboard.add(next_button)
    if not next_meme and prev_meme:
        keyboard.add(prev_button)    
    save_button = types.InlineKeyboardButton(responses[utils.lang(cid)]['delete_meme'], callback_data=f'unsave {meme}')
    keyboard.add(save_button)
    bot.edit_message_media(types.InputMediaPhoto(meme, caption=f'<code>{meme}</code>', parse_mode='html'), cid, mid, reply_markup=keyboard)
