# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['meme'], 
    func=lambda m: 
        utils.is_recent(m) and 
        utils.is_user(m.chat.id) and 
        not utils.is_banned(m.chat.id)
    )
def command_meme(m):
    cid = m.chat.id
    uid = m.from_user.id
    meme = utils.random_meme(cid)
    if meme:
        bot.send_photo(cid, meme, caption=f'#{meme}')
    else:
        bot.send_message(cid, responses[utils.lang(cid)]['no_more'])
