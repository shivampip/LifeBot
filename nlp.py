from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer


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
        return self.lemmatizer.lemmatize(self.msg)
    

if __name__=='__main__':
    lang= Lang()
    lang.setMsg("oxes")
    print(lang.lemma())