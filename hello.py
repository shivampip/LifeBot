import mytube as mt 
import os
import pyglet
from pytube.helpers import safe_filename
import glob
import c

import logging as log 
log.basicConfig(level=log.INFO, format= c.LOG_FORMAT)

def getSize(ss):
    fsize= ss/1000000
    return round(fsize,2)

def is_downloaded(fname):
	fname= safe_filename(fname)
	for file in glob.glob('Files/Musics/*.*'):
		li= file.rindex('.')
		name= file[13:li]
		if(name==fname):
			return file
	return "NO"
 



def playSong(title, fpath):
	log.info("Playing "+safe_filename(title))
	song= pyglet.resource.media(fpath,streaming=False)
	song.play()
	pyglet.app.run() 

	

def download(v):
	link= v.url
	ress= mt.getAllStreams(link)
	audio_streams=[]
	for r_stream in ress:
		if(r_stream.type=='audio'):
			audio_streams.append(r_stream)
	r= audio_streams[0]
	mt.downloadM(r)
	fpath= str(os.path.join('Files/Musics',safe_filename(v.title)))+'.'+r.subtype
	#playSong(v.title, fpath)
	return fpath
  


"""
text= input("Enter Video Name:- ")

videos= mt.search_youtube(text)

v= videos[0]

bolo= is_downloaded(v.title)
if(bolo=='NO'):
	print("Downloading ",v.title)
	download(v)
else:
	playSong(v.title, bolo)
"""

def giveInfo(v):
	link= v.url
	ress= mt.getAllStreams(link)
	audio_streams=[]
	for r_stream in ress:
		if(r_stream.type=='audio'):
			audio_streams.append(r_stream)
	r= audio_streams[0]
	size= getSize(r.filesize)
	return size, str(size)+"MB"


def giveTitle(songName):
    videos= mt.search_youtube(songName)
    v= videos[0]
    size, sizes= giveInfo(v)
    data= '*Name:* '+v.title+'\n*Size:* '+sizes+'\n*Duration:* '+v.duration
    legel= size<=c.SIZE_LIMIT 
    if(not legel):
    	data+="\n`File size should be less than "+str(c.SIZE_LIMIT)+" MB`\n*Try with another keyword*"
    else:
    	data+="\n`Downloading, Please wait`"
    return legel, data

def giveMe(songName):
    videos= mt.search_youtube(songName)
    v= videos[0]
    bolo= is_downloaded(v.title)
    if(bolo=='NO'):
        log.info("Downloading "+v.title)
        return download(v)
    else:
    	log.info("Already Downloaded")
    	return bolo


