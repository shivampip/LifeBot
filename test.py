import processor


txt= "words my name is Shivam Agrawal"


msg= processor.Message()
msg.setMsg(txt)
print(msg.process())