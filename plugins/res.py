# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['res'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_res(m):
    cid = m.chat.id
    if len(m.text.split()) == 1:
        bot.send_message(cid, "Error. Debes introducir `/res _[!]_ _<mensaje>_` | Empieza el mensaje con *!* para usar Markdown", parse_mode="Markdown")
        return
    msg = m.text.split(None, 1)[1]
    parse_mode = "Markdown" if msg.startswith('!') else None
    m_text = m.reply_to_message.text.split('\n') if m.reply_to_message.text else m.reply_to_message.caption.split('\n')
    m_id = m_text[5].split(': ')[1]
    c_id = m_text[6].split(': ')[1]
    answer = f"{responses[utils.lang(c_id)]['admin_response']}:\n\n{msg.lstrip('!')}"
    try:
        bot.send_message(
            c_id,
            answer,
            parse_mode=parse_mode,
            reply_to_message_id=m_id)
    except Exception as e:
        bot.send_message(
            52033876,
            utils.send_exception(e),
            parse_mode="Markdown")