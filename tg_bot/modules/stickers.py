import os
from telegram import Message, Chat, Update, Bot
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async
from telegram.utils.helpers import escape_markdown

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.filters import CustomFilters


@run_async
def stickerid(bot: Bot, update: Update):
    msg = update.effective_message
    if msg.reply_to_message and msg.reply_to_message.sticker:
        update.effective_message.reply_text("Sticker ID:\n```" + 
                                            escape_markdown(msg.reply_to_message.sticker.file_id) + "```",
                                            parse_mode=ParseMode.MARKDOWN)
    else:
        update.effective_message.reply_text("Please reply to a sticker to get its ID.")


@run_async
def getsticker(bot: Bot, update: Update):
    msg = update.effective_message
    chat_id = update.effective_chat.id
    if msg.reply_to_message and msg.reply_to_message.sticker:
        file_id = msg.reply_to_message.sticker.file_id
        newFile = bot.get_file(file_id)
        newFile.download('sticker.png')
        bot.sendDocument(chat_id, document=open('sticker.png', 'rb'))
        os.remove("sticker.png")
        
    else:
        update.effective_message.reply_text("Please reply to a sticker for me to upload its PNG.")

__help__ = """
Fetching ID of stickers is made easy! With this stickers command you simply can \
fetch ID of sticker.

 - /stickerid: reply to a sticker to me to tell you its file ID.
 - /getsticker: reply to a sticker and get that sticker as .png and image.

"""

__mod_name__ = "Stickers"

STICKERID_HANDLER = DisableAbleCommandHandler("stickerid", stickerid)
GETSTICKER_HANDLER = DisableAbleCommandHandler("getsticker", getsticker, filters=CustomFilters.sudo_filter)

dispatcher.add_handler(STICKERID_HANDLER)
dispatcher.add_handler(GETSTICKER_HANDLER)
