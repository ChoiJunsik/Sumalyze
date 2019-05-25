import pytube
from pydub import AudioSegment

def youtubeToAudio(url):
    yt = pytube.YouTube(url)
    vids= yt.streams.filter(mime_type='video/mp4',audio_codec='mp4a.40.2').order_by('resolution').desc().all()
    vids[0].download('C:\sumalyze\media\\')
    vName = 'C:\sumalyze\media\\'+vids[0].default_filename
    sound = AudioSegment.from_file(vName)
    sound.export('C:\sumalyze\media\\'+vids[0].default_filename+'.mp3', format="mp3")

    return vName
