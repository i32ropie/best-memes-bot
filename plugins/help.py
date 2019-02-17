# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['help'],
    func=lambda m: 
        utils.is_recent(m) and 
        utils.is_user(m.chat.id) and 
        not utils.is_banned(m.chat.id)
    )
def command_help(m):
    cid = m.chat.id
    bot.send_message(cid, responses[utils.lang(cid)]['help'])
