from config import bot, admins, utils
import importdir
import sys

if sys.version_info.major < 3:
    raise Exception('Must be using Python 3')

importdir.do('plugins', globals())

try:
    for cid in admins:
        bot.send_message(cid, "@best_memes_bot ha sido encendido.")
except Exception as e:
    for cid in admins:
        bot.send_message(cid, utils.send_exception(e), parse_mode="Markdown")

bot.polling(none_stop=True, interval=0, timeout=3)
