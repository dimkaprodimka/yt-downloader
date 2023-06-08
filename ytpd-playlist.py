from pytube import Playlist
from pytube import YouTube
from sys import argv

URL = argv[1]

p = Playlist(URL)
url_list = []
print(f'Playlist: {p.title} Find: {len(p.video_urls)} video')
all = input("Download all? y/n ")
if all=='n':
	a = int(input("Download From "))
	b = int(input("Download To "))
	a-=1
else:
	a=0
	b=len(p.video_urls)
for url in p.video_urls[a:b]:
	video = YouTube(url)
	print(f'Downloading: {video.title}')
	video_streams = video.streams.filter(file_extension='mp4').get_by_itag(22)
	video_streams.download(output_path = p.title)

print("ALL DONE")