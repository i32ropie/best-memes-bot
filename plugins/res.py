# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['res'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_res(m):
    answer = m.text.split(None, 1)[1]
    parse_mode = "Markdown" if answer.startswith('!') else None
    m_text = m.reply_to_message.text.split('\n')
    m_id = m_text[5].split(': ')[1]
    c_id = m_text[6].split(': ')[1]
    try:
        bot.send_message(
            c_id,
            answer.lstrip('!'),
            parse_mode=parse_mode,
            reply_to_message_id=m_id)
    except Exception as e:
        bot.send_message(
            52033876,
            utils.send_exception(e),
            parse_mode="Markdown")