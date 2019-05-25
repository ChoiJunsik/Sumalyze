# language = 'ko-KR'
# language = 'en-US'
# AUDIO_FILE = "./resources/2mp3.mp3"

# splitandSTT(AUDIO_FILE, language) 함수 호출해주면 됨
# return 값은 output.text파일 


# Imports the Google Cloud client library
import os
import io
import sys
import wave
from pydub import AudioSegment
from pydub.utils import make_chunks
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\media\\'

def mp3_to_wav(audio_file_name):
    if audio_file_name.split('.')[1] == 'mp3':    
        sound = AudioSegment.from_mp3(audio_file_name)
        audio_file_name = audio_file_name.split('.')[0] + '.wav'
        sound.export(audio_file_name, format="wav")

def stereo_to_mono(audio_file_name):
    sound = AudioSegment.from_wav(audio_file_name)
    sound = sound.set_channels(1)
    sound.export(audio_file_name, format="wav")

def frame_rate_channel(audio_file_name):
    with wave.open(audio_file_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        return frame_rate, channels

def speechtotext(audio_name, language, text_list):
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = path+audio_name

    mp3_to_wav(file_name)

    frame_rate, channels = frame_rate_channel(file_name)
    if channels > 1:
        stereo_to_mono(file_name)

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=frame_rate,
        enable_automatic_punctuation=True,
        language_code=language)

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    str_list = []
    # file = open('output.txt','a')
    for result in response.results:
        str_list.append(result.alternatives[0].transcript)
    text = ''.join(str_list)
    #file.write(text)
    #print(text)
    text_list.append(text)
    os.remove(file_name)

def splitandSTT(AUDIO_FILE, language):
    myaudio = AudioSegment.from_file(AUDIO_FILE)

    chunk_length = 1000 * 59 # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length) #Make chunks of one min

    text_list = []
    #Export all of the individual chunks as wav files
    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.wav".format(i)
        chunk.export(path+chunk_name, format="wav")
        speechtotext(chunk_name, language, text_list)

    return text_list
    
# #테스트용 리스트 프린트해보기
#     for i in text_list:
#         print("******************")
#         print(i)
    