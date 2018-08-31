"""
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#post-an-image-file-from-disk
"""

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)

import processor
import sender
import logging as log 
import c

log.basicConfig(level=log.INFO, format= c.LOG_FORMAT)
"""
log= logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler('botlog.log'))
"""

#log.basicConfig(level=log.INFO, filename='botlog.log')




log.info("Program started")
updater= Updater("641238067:AAEB___d1oM4llx6XzaWzxe4g9CAomVN-P0")
   
def textpro(bot, update):
    log.info("msg received:")
    pro= processor.Processor()
    pro.get([bot, update])


updater.dispatcher.add_handler(MessageHandler(Filters.text, textpro))
log.info("Dispatcher attached.")


def notify(bot, update, msg):
    chatid= update.message.chat.id
    sen= sender.Sender(chatid, bot, update)
    sen.sendText(msg+"\n:(")

def error_callback(bot, update, error):
    try:
        raise error
    except Unauthorized:
        log.warn("Unauthorized")
        notify(bot, update, "Unauthorized")
        # remove update.message.chat_id from conversation list
    except BadRequest:
        log.warn("BadRequest")
        notify(bot, update, "BadRequest")
        # handle malformed requests - read more below!
    except TimedOut:
        log.warn("TimedOut")
        notify(bot, update, "TimedOut")
        # handle slow connection problems
    except NetworkError:
        log.warn("NetworkError")
        notify(bot, update, "NetworkError")
        # handle other connection problems
    except ChatMigrated as e:
        log.warn("ChatMigrated "+e)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        log.warn("TelegramError")
        notify(bot, update, "TelegramError")
        # handle all other telegram related errors

updater.dispatcher.add_error_handler(error_callback)




updater.start_polling()
log.info("Polling started")
updater.idle()
log.info("IDLE")
