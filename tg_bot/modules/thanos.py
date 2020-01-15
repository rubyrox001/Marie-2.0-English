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

def thanos(bot: Bot, update: Update):
    tony = requests.get('http://api.othanos.ru/noise/1').json()[0]["preview"]
    final = "http://media.othanos.ru/{}".format(tony)
    update.message.reply_photo(final)
		
THANOS_HANDLER = DisableAbleCommandHandler("thanos", thanos)
dispatcher.add_handler(THANOS_HANDLER)
