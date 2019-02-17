# -*- coding: utf-8 -*-

from config import *

@bot.message_handler(
    commands=['github'],
    func=lambda m: 
        utils.is_admin(m.from_user.id)
    )
def command_github(m):
    cid = m.chat.id
    pull_info = os.popen("git pull").read()
    bot.send_message(cid, pull_info)
    if not pull_info.startswith("Already"):
        os.popen("kill -9 `ps aux | grep bot | grep -v grep |  awk '{print $2}'`")
