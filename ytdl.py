from pytube import YouTube
from pytube.cli import on_progress
import os

yt = YouTube(str(input("Enter the URL of the video to be downloaded: \n>> ")), on_progress_callback=on_progress)

video = yt.streams.filter(only_audio=True).first();

print("Enter destination folder")
folder = str(input(">> ")) or '.'

out_file = video.download(output_path=folder)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " downloaded");
