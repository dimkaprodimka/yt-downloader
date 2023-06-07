from pytube import YouTube
from sys import argv

URL = argv[1]
video = YouTube(URL)
print(f'Downloading: {video.title}')
video_streams = video.streams.get_by_itag(22)
video_streams.download()
print("ALL DONE")
