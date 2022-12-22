from pytube import YouTube
from sys import argv

link = input()
yt = YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()
yd.download(r'\Users\jolec\Desktop\Pobrane z yt')
