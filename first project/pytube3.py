from pytube import YouTube
# link = input("Enter the YouTube video URL: ")
# youtubeVideo = YouTube(link)
# youtubeVideo = youtubeVideo.streams.get_highest_resolution()
# try:
#     youtubeVideo.download()
# except:
#     print("error")
# print("Downloaded")
def download():
    video_link=input("Enter youtube url ")
    yt = YouTube(video_link)
    song= yt.streams.filter(only_audio=True).first()
    song.download()
    print("downloaded")
download()
