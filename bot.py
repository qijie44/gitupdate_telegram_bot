from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import configparser
import logging
import os
import sys
#import bus_timing as bt

config = configparser.ConfigParser()
config.read("bot.ini")

updater = Updater(token=config["KEYS"]["BOT_TOKEN"], use_context="true")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id= update.effective_chat.id, text="I'm a bot, please talk to me!")
    print(update.effective_user.id)

def update_bot(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Updating now, going for a nap")
    pid = os.fork()
    if pid == 0:
        os.system("./update_bot.sh")
    updater.stop()
    sys.exit()
    context.bot.send_message(chat_id=update.effective_chat.id, text="i'm still running!")


start_handler = CommandHandler("start", start)
update_handler = CommandHandler("update", update_bot)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(update_handler)

updater.start_polling()
