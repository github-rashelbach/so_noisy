from pytube import YouTube
from vimeo_downloader import Vimeo
import logging
import vimeodownload
try:



    response = vimeodownload.get_video("https://vimeo.com/503166067")
    exit
    video = Vimeo('https://vimeo.com/503166067')
    logging.info("Downloading {}".format(video.metadata.title))
    stream = video.streams[0]
    path = "/dev/null"
    stream.download()

    yt1 = YouTube('http://www.youtube.com/watch?v=fHnoQVAk7n0')
    logging.info("Downloading {}".format(yt1.title))
    stream = yt1.streams.get_by_itag(18)
    path = "/dev/null"
    stream.download('','','',False)





except:
    print(f"Err: {error}")
