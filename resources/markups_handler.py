# --------------------------------------------- #
# Plugin Name           : Telegram Support Bot  #
# Author Name           : fabston               #
# Fixed Bugs            : vi-dev0               #
# File Name             : markups_handler.py    #
# --------------------------------------------- #

import config
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def faqButton():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Read our FAQ\'s', callback_data='faqCallbackdata'))
    return markup
