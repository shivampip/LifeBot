from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import sender
import wiki
import hello
import book
import logging as log
import c

log.basicConfig(level=log.INFO, format= c.LOG_FORMAT,handlers=[ log.StreamHandler(), log.FileHandler(c.LOG_PATH+'/'+c.LOG_FILE+'.log')])
#log.info('Logging Started')
#===============================================================


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
        elif(self.msg.startswith("book")):
            """n= 2
            try:
                n= int(self.msg[5])
                name= self.msg[7:]
            except Exception as e:
                n= 2"""
            name= self.msg[5:]
            bk= book.Book()
            bk.search(name)
            self.send(mtype='text', msg= 'Downloading books.\nPlease wait')
            urls= bk.process()
            for url in urls:
                self.send(mtype='doc', params=[url])

        elif("i love you" in self.msg):
            self.send(mtype='mtext', msg= "`But I don't love you`")
        elif(self.msg.startswith("hello")):
            self.send(mtype='mtext', msg= c.HELP_MSG)
        else:
            self.send(mtype='text', msg='No match found')
        log.info('='*40+ '\n')

#============================================================================================
#============================================================================================

    def get(self, params): 
        self.bot= params[0]
        self.update= params[1]
        self.msg= self.update.message.text.lower()
        self.senName= self.update.message.from_user.first_name
        log.info("{"+self.senName+"} Message: "+self.msg)
        self.process()

    

