# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['reload'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_reload(m):
    cid = m.chat.id
    bot.send_message(cid, "Reiniciando el bot...")
    os.popen("kill -9 `ps aux | grep bot | grep -v grep |  awk '{print $2}'`")
