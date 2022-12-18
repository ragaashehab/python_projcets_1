# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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