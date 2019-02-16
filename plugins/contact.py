# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['contact'],
    func=lambda m: 
        utils.is_recent(m) and 
        utils.is_user(m.chat.id) and 
        not utils.is_banned(m.chat.id)
    )
def command_contact(m):
    cid = m.chat.id
    bot.send_message(cid, responses[utils.lang(cid)]["contact_1"], reply_markup=types.ForceReply(True), reply_to_message_id=m.message_id)
    user_step[str(cid)] = "contact"