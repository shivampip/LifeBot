import wiki
import nlp
import song
import datetime

class Message:
    
    def __init__(self):
        print("[ Inilizing Message ]")
        self.msg= nlp.Lang()
        
    def print(self):
        print("\nUser: "+self.msg)
        
    def setMsg(self, msg):
        print('\nUser: '+msg)
        self.msg.setMsg(msg.lower())
        #self.msg.process()
    
    def log(self):
        file= open("log.txt",'a')
        file.write("\n["+str(datetime.datetime.now())+"] ["+self.fname+"] "+self.msg.txt)
        file.close()
        print("[logged]")
    
    def setBot(self, bot, update):
        self.bot= bot
        self.update= update
        self.fname= update.message.from_user.first_name
        self.log()
    
    def process(self):
        out=""
        if(self.msg.txt.startswith("wiki")):
            out= wiki.getSummery(self.msg.txt[5:])
        elif(self.msg.txt.startswith("words")):
            out= str(self.msg.words)
        elif(self.msg.txt.startswith("play")):
            print("[ Playing "+self.msg.txt[5:]+" ]")
            pass
        elif(self.msg.txt.startswith("song")):
            name= self.msg.txt[5:]
            print("Song: ",name)
            self.update.message.reply_text("Downloading "+song.getName(name)+"\nPlease wait..")
            sname= song.get(name)
            chatid= self.update.message.chat.id
            self.bot.send_audio(chat_id=chatid, audio=open(sname, 'rb'))
            
        else:
            out= "Format not recognised"
            
        print("\nLife : "+out)
        return out