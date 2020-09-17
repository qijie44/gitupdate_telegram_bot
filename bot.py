from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import configparser

config = configparser.ConfigParser()
config.read("bot.ini")