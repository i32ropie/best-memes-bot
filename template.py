# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['command'],
    func=lambda m: 
        utils.is_recent(m) and 
        utils.is_user(m.chat.id) and 
        not utils.is_banned(m.chat.id)
    )
def command_COMMAND(m):
    cid = m.chat.id
    uid = m.from_user.id
    # Code
