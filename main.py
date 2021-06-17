from multiprocessing import cpu_count
from youtube_dl import YoutubeDL

VIDEO_LINK = "https://www.youtube.com/watch?v=M5v1nXiUaOI"
OPTIONS = {
    "format": "bestaudio",
    # "outtmpl": f"{title}",
}

# todo:
# specify number of threads
# specify .mp3 format
# https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L121-L269

downloader = YoutubeDL(OPTIONS)
meta = downloader.extract_info(VIDEO_LINK, download=False)
title = meta["title"].replace(" ", "_").lower()
channel = meta["uploader"].replace(" ", "_").lower()
print(channel + "--" + title)
