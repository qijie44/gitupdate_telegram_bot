from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import configparser
import logging
import subprocess

config = configparser.ConfigParser()
config.read("bot.ini")

updater = Updater(token=token, use_context="true")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id= update.effective_chat.id, text="I'm a bot, please talk to me!")
    print(update.effective_user.id)

def update_bot(update, context):
    subprocess.call("update_bot.sh")
    exit()
    pass
