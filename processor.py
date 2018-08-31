from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import sender
import wiki
import c
import hello

#===============================================================
import logging as log 
log.basicConfig(level=log.INFO, format= c.LOG_FORMAT)

class Processor:

    def __init__(self):  
        pass

    def send(self, mtype, msg=None, params=None):
        chatid= self.update.message.chat.id
        sen= sender.Sender(chatid, self.bot, self.update)
        
        if(mtype=='text'):
            sen.sendText(msg)    
        elif(mtype=='mtext'):
            sen.sendTextM(msg)
        elif(mtype=='img'): 
            url= params[0]
            sen.sendImg(url)
        elif(mtype=='audio'): 
            url= params[0]
            sen.sendAudio(url)
        elif(mtype=='video'): 
            url= params[0]
            sen.sendVideo(url)
        elif(mtype=='doc'):
            url= params[0]
            sen.sendDoc(url) 

#============================================================================================
#============================================================================================

    def process(self):
        log.info("Processing msg")
        if(self.msg.startswith('wiki')):
            summary= wiki.getSummery(self.msg[5:])
            self.send(mtype='text', msg= summary)
        elif(self.msg.startswith('song')):
            sname= self.msg[5:]
            legel, rname= hello.giveTitle(sname)
            self.send(mtype='mtext', msg= rname)
            if(legel):
                spath= hello.giveMe(sname)
                self.send(mtype='audio', params=[spath])

        else:
            self.send(mtype='text', msg='No match found')
        log.info('='*20)

#============================================================================================
#============================================================================================

    def get(self, params): 
        self.bot= params[0]
        self.update= params[1]
        self.msg= self.update.message.text.lower()
        log.info("Message: "+self.msg)
        self.process()

    

