from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import logging as log
import c

log.basicConfig(level=log.INFO, format= c.LOG_FORMAT,handlers=[ log.StreamHandler(), log.FileHandler(c.LOG_PATH+'/'+c.LOG_FILE+'.log')])
#log.info('Logging Started')

class Lang:
    
    def __init__(self):
        self.lemmatizer= WordNetLemmatizer()
        print("[ NLP Inilized ]")
        
    def print(self):
        print("Raw data is "+self.msg)
        
    def setMsg(self, msg):
        self.msg= msg
        self.process()
    
    def process(self):
        self.txt= self.msg
        self.sents= sent_tokenize(self.msg)
        self.words= word_tokenize(self.msg)
        
    def lemma(self):
        #return self.lemmatizer.lemmatize(self.msg, pos='a') #better -> good
        return self.lemmatizer.lemmatize(self.msg)
    

if __name__=='__main__':
    lang= Lang()
    lang.setMsg("")
    
    words= ['oxes', 'cats', 'better', 'best', 'more beautiful']
    for word in words:
        lang.setMsg(word)
        print(lang.lemma())