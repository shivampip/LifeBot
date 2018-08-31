import os
import sys
from pytube import YouTube
import urllib
import requests
from bs4 import BeautifulSoup
import subprocess

class YoutubeMetadata:
    """A data store to store the information of a youtube video."""

    SPACE = "#"

    def __init__self(self):
        self.title = ""
        self.url = ""
        self.duration = ""
        self.hash = ""


def search_youtube(query):
    """Behold the greatest magic trick ever : crawl and crawl."""
    print("Searching youtube for :: {}".format(query))
    base_url = "https://www.youtube.com"
    url = base_url + "//results?sp=EgIQAVAU&q=" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    videos = []
    for tile in soup.find_all(attrs={'class': "yt-lockup-tile"}):
        yt_uix_tile = tile.find(attrs={'class': 'yt-uix-tile-link'})
        youtube_metadata = YoutubeMetadata()
        youtube_metadata.url = base_url + yt_uix_tile['href']
        youtube_metadata.title = yt_uix_tile['title']
        description = tile.find("div", {'class': 'yt-lockup-description'})
        youtube_metadata.description = description.get_text().strip() if description else "No description available"
        duration = tile.find("span", {'class': 'video-time'})
        youtube_metadata.duration = duration.get_text() if duration else "uknown duration"
        videos.append(youtube_metadata)
    return videos

def getFirstStream(link):
	yt = YouTube(link)
	return yt.streams.first()

def getAllStreams(link):
	yt= YouTube(link)
	return yt.streams.all()

def downloadV(stream):
    try:
        os.mkdir("Videos")
    except Exception as e:
        pass
    print("Downloading, Please wait....")
    stream.download(os.path.join(os.getcwd(),'Videos'))
    print("Downloaded Successfully.")
    return


# subprocess.Popen(r'explorer /select,"D:\LTI\OLD"')

def downloadM(stream):
    try:
        os.mkdir("Musics")
    except Exception as e:
        pass
    stream.download(os.path.join(os.getcwd(),'Musics'))
    return

