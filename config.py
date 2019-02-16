import os
import json
import telebot
import logging
from telebot import types
from pymongo import MongoClient
from collections import OrderedDict
import time
import utils

client = MongoClient('localhost:27017')
db = client.memes

conf = db.config
users = db.users
memes = db.memes

bot = telebot.TeleBot(utils.get_config_item('token'))
telebot.logger.setLevel(int(utils.get_config_item('logging_level')))

admins = utils.get_config_item('admins')
mods = utils.get_config_item('mods')

responses = {x.split('.')[0]:json.load(open('locale/{}'.format(x), encoding='utf-8'), object_pairs_hook=OrderedDict) for x in os.listdir('locale')}

user_step = dict()