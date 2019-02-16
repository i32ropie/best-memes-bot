import traceback
import time
import sys
import config


def get_user_step(uid):
    if str(uid) not in config.user_step or is_banned(uid):
        config.user_step[str(uid)] = 0
    return config.user_step[str(uid)]


def random_meme(uid = None):
    # We search for a new random meme, excluding the list of memes already seen by the user
    exclude = config.users.find_one(str(uid))['memes'] if is_user(uid) else []

    query = config.memes.aggregate([
        {
            "$match": {
                "_id" : {
                    "$nin" : exclude
                }
            }
        },
        {
            "$sample": {
                "size": 1
            }
        }
    ])
    
    meme = query.next() if query.alive else None

    # If we find a meme, we retrieve it ...
    if meme:
        # ... increment the views of the meme ...
        config.memes.update(
            {
                "_id": meme["_id"]
            },
            {
                "$inc": {
                    "views": 1
                }
            }
        )
        # ... and add the meme as seen to the user
        config.users.update(
            {
                "_id": str(uid)
            },
            {
                "$push": {
                    "memes": meme['_id']
                }
            }
        )
    return meme['_id'] if meme else meme

def was_user(cid):
    return config.users.find_one(str(cid)) is not None and config.users.find_one(str(cid))['active'] == False


def is_user(cid):
    return config.users.find_one(str(cid)) is not None and config.users.find_one(str(cid))['active'] == True


def lang(uid):
    if config.users.find_one(str(uid)):
        return config.users.find_one(str(uid))['lang']
    else:
        return 'en'


def is_admin(uid):
    return str(uid) in config.admins


def is_mod(uid):
    return str(uid) in config.mods+config.admins


def is_banned(cid):
    if is_user(cid):
        return config.users.find_one(str(cid))['banned']
    else:
        return False


def get_config_item(key):
    item = config.conf.find_one({"key": key})
    if item:
        return item['value']
    else:
        return None


def is_recent(m):
    return (time.time() - m.date) < 5


def line(alt=False):
    if alt:
        return u'\n—————————————————————————\n'
    else:
        return u'\n`—————————————————————————`\n'


def send_exception(exception):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    tb = traceback.extract_tb(exc_tb, 4)
    message = '\n`' + str(exc_type) + '`'
    message += '\n\n`' + str(exc_obj) + '`'
    for row in tb:
        message += line()
        for val in row:
            message += '`' + str(val) + '`\n'
    return message


def is_int(s):
    if not s:
        return False
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def contact_format(m):
    name = m.from_user.first_name
    alias = str(m.from_user.username)
    cid = str(m.chat.id)
    uid = str(m.from_user.id)
    m_id = str(m.message_id)
    msg = m.text
    if cid == uid:
        txt = "Nuevo mensaje\n\nNombre: " + name + "\nAlias: @" + alias + "\nIdioma: " + \
            lang(cid) + "\nM_ID: " + m_id + "\nID: " + cid + "\n\nMensaje: " + msg
    else:
        txt = "Nuevo mensaje\n\nNombre: " + name + "\nAlias: @" + alias + "\nIdioma: " + lang(
            cid) + "\nM_ID: " + m_id + "\nID: " + cid + "\nUID: " + uid + "\n\nMensaje: " + msg
    return txt