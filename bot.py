"""
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#post-an-image-file-from-disk
"""

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import processor



print("Welcome to AI")
updater= Updater("641238067:AAEB___d1oM4llx6XzaWzxe4g9CAomVN-P0")

msg= processor.Message()

def hello(bot, update):
    update.message.reply_text('Hello {}, how are you?'.format(update.message.from_user.first_name))
    
def textpro(bot, update):
    msg.setMsg(update.message.text)
    msg.setBot(bot, update)
    out= msg.process()
    update.message.reply_text(out)

def stop(bot, update):
    print("Stopping")
    updater.stop()
    
def photo(bot, update):
    chatid= update.message.chat.id
    print(chatid)
    bot.send_audio(chat_id=chatid, audio=open('rab.mp4', 'rb'))
    #bot.send_photo(chat_id=chatid, photo=open('taj.jpeg', 'rb'))
    #bot.send_photo(chat_id=chatid, photo='https://telegram.org/img/t_logo.png')
    #update.message.reply_text("Your userid is "+update.message.from_user.id)
    
    
updater.dispatcher.add_handler(CommandHandler('hola', hello))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('foto', photo))

updater.dispatcher.add_handler(MessageHandler(Filters.text, textpro))


updater.start_polling()
updater.idle()
