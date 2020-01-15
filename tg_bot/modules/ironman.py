from telegram import ChatAction
import html
import urllib.request
import re
import json
from typing import Optional, List
import time
import urllib
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote_plus, urlencode
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from tg_bot import dispatcher
from tg_bot.__main__ import STATS, USER_INFO
from tg_bot.modules.disable import DisableAbleCommandHandler

def ironman(bot: Bot, update: Update):
    tony = requests.get('http://api.oironman.ru/noise/1').json()[0]["preview"]
    final = "http://media.oironman.ru/{}".format(tony)
    update.message.reply_photo(final)
		
__help__ = """
 - /ironman: Sends Random Ironman pic.
"""
__mod_name__ = "TONY"
IRONMAN_HANDLER = DisableAbleCommandHandler("ironman", ironman)
dispatcher.add_handler(IRONMAN_HANDLER)
