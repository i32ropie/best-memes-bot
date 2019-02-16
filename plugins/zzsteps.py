# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(func=lambda m: utils.get_user_step(m.chat.id) == 'contact' and m.content_type == 'text')
def step_contact(m):
    cid = m.chat.id
    user_step[str(cid)] = 0
    for x in admins:
        bot.send_message(x, utils.contact_format(m))
    bot.send_message(cid, responses[utils.lang(cid)]['contact_2'])