import wiki
import nlp

class Message:
    
    def __init__(self):
        print("[ Inilizing Message ]")
        self.msg= nlp.Lang()
        
    def print(self):
        print("\nUser: "+self.msg)
        
    def setMsg(self, msg):
        print('\nUser: '+msg)
        self.msg.process(msg.lower())
        
    def process(self):
        out=""
        if(self.msg.txt.startswith("wiki")):
            out= wiki.getSummery(self.msg.txt[5:])
        elif(self.msg.txt.startswith("words")):
            out= str(self.msg.words)
        elif(self.msg.txt.startswith("play")):
            print("[ Playing "+self.msg.txt[5:]+" ]")
            pass
        else:
            out= "Format not recognised"
            
        print("\nLife : "+out)
        return out