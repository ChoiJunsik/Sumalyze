import pytube
from pydub import AudioSegment
import os
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\media\\'

def youtubeToAudio(url):
    yt = pytube.YouTube(url)
    vids= yt.streams.filter(mime_type='video/mp4',audio_codec='mp4a.40.2').order_by('resolution').desc().all()
    vids[0].download(path)
    vName = path+vids[0].default_filename
    sound = AudioSegment.from_file(vName)
    sound.export(vName+'.mp3', format="mp3")

    return vName
