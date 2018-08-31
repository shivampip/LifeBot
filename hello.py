import mytube as mt 
import os
import pyglet
from pytube.helpers import safe_filename
import glob


def getSize(ss):
    fsize= ss/1000000
    return round(fsize,2)

def is_downloaded(fname):
	fname= safe_filename(fname)
	for file in glob.glob('Musics/*.*'):
		li= file.rindex('.')
		name= file[7:li]
		if(name==fname):
			return file
	return "NO"
 



def playSong(title, fpath):
	print("Playing",safe_filename(title))
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
	fpath= str(os.path.join('Musics',safe_filename(v.title)))+'.'+r.subtype
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

def giveMe(songName):
    videos= mt.search_youtube(songName)
    v= videos[0]
    bolo= is_downloaded(v.title)
    if(bolo=='NO'):
        print("Downloading ",v.title)
        return download(v)
    else:
        return bolo


