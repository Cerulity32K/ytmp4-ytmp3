from pytube import *
from moviepy.editor import *
import os
import random

alpha: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def randstr(l: int, string: str = alpha):
    ret = ""
    strlen  = len(string)-1
    for i in range(l):
        ret += string[random.randint(0,strlen)]
    return ret

url = input("Enter the URL of the video you want to download: ")
outputname = input("Enter the name of the file (Leave empty for auto-generated title): ") or "output"+randstr(25, alpha)

yt = YouTube(
    str(url))

print("Getting video stream...")
video = yt.streams.get_highest_resolution()

print("Downloading video...")
out_file = video.download(filename=outputname+".mp4")

print(yt.title + " has been successfully downloaded.")

print("Grabbing saved MP4 file...")
vid = VideoFileClip(outputname+".mp4")

print("Isolating audio...")
audio = vid.audio

print("Saving audio...")
audio.write_audiofile(outputname + ".mp3")

print("Closing audio...")
audio.close()

print("Closing video...")
vid.close()

print(yt.title + "has been converted to MP3.")