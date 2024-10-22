"""
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#post-an-image-file-from-disk
https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html#telegram.Bot.send_document
"""

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)

import processor
import sender
import logging as log
import c
import shiva

log.basicConfig(level=log.INFO, format= c.LOG_FORMAT,handlers=[ log.StreamHandler(), log.FileHandler(c.LOG_PATH+'/'+c.LOG_FILE+'.log')])
log.info('Logging Started')
"""
log= logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler('botlog.log'))
"""

#log.basicConfig(level=log.INFO, filename='botlog.log')



log.info("Program started")
updater= Updater(shiva.BOT_TOKEN)  #Bot Token is given by BotFather on Telegram while creating bot. (It can't be shared)
   
def textpro(bot, update):
    pro= processor.Processor()
    pro.get([bot, update])


updater.dispatcher.add_handler(MessageHandler(Filters.text, textpro))
log.info("Dispatcher attached.")


def notify(bot, update, msg):
    chatid= update.message.chat.id
    sen= sender.Sender(chatid, bot, update)
    sen.sendTextM(msg+"\n`If you know Shivam, tell him`")

def error_callback(bot, update, error):
    log.error(str(error))
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

