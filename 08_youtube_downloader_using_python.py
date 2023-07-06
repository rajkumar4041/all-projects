from pytube import YouTube 

link ="paste link here "
youtube_1=YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos=youtube_1.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)

print()
strm=int(input("enter : "))
videos[strm].download
print("download successfully . ")


#for play list 
# from pytube import Playlist

# py=Playlist("link paste ")

# print(f"Downloading : {py.title}")

# for video in py.videos : 
#     video.streams.first().download()