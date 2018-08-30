from nltk.tokenize import word_tokenize, sent_tokenize

class Lang:
    
    def __init__(self):
        print("[ NLP Inilized ]")
        
    def print(self):
        print("Raw data is "+self.msg)
        
    def process(self, msg):
        self.msg= msg
        self.txt= msg
        self.sents= sent_tokenize(msg)
        self.words= word_tokenize(msg)
        pass