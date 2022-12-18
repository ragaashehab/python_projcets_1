
from pytube import YouTube
from sys import argv

if __name__ == '__main__':
    link = input("Enter your youtube URL to download: ").strip()  #argv[1]
    yt = YouTube(link)

    print("Title: ", yt.title)

    print("View: ", yt.views)

    yd = yt.streams.get_highest_resolution()

    # ADD FOLDER HERE
    yd.download('./YTfolder')
