# -*- coding: utf-8 -*-

from config import *
from io import StringIO

@bot.message_handler(
    commands=['exec'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_exec(m):
    cid = m.chat.id
    if len(m.text.split()) == 1:
        bot.send_message(
                cid,
                "Uso: /exec _<code>_ - Ejecuta el siguiente bloque de código.",
                parse_mode="Markdown")
        return
    cout = StringIO()
    utils.sys.stdout = cout
    cerr = StringIO()
    utils.sys.stderr = cerr
    code = ' '.join(m.text.split(' ')[1:])
    try:
        exec(code)
    except Exception as e:
        bot.send_message(cid, utils.send_exception(e), parse_mode="Markdown")
    else:
        if cout.getvalue():
            bot.send_message(cid, str(cout.getvalue()))
    utils.sys.stdout = utils.sys.__stdout__
    utils.sys.stderr = utils.sys.__stderr__
