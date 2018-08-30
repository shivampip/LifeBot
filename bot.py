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
    out= msg.process()
    update.message.reply_text(out)


    
updater.dispatcher.add_handler(CommandHandler('hola', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, textpro))


updater.start_polling()
updater.idle()
