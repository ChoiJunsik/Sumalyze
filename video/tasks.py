from __future__ import absolute_import
from sumalyze.celery import app
from celery import shared_task
from django.shortcuts import render, get_object_or_404,redirect
from .yToA import youtubeToAudio
import os
import io
import sys
import wave
import re
from .speechToText import *
from sumalyze.ibmContent import ibmContent
from .models import VideoPost
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

@shared_task
def videoSumalyze(pk):
    post = get_object_or_404(VideoPost, pk=pk)
    lang = 'en-US'    
    if post.lang == '한국어':
        lang = 'ko-KR'
    from lexrankr import LexRank
    lexrank = LexRank()
    chunk = []
    chunk2 = []
    url = post.url
    path = youtubeToAudio(url)
    post.title = re.sub('[^가-힣\\s]', '', str(path))
    chunk = splitandSTT(path, lang)
    text = " ".join(chunk)
    os.remove(path+'.mp3')
    os.remove(path)

    #요약 적용
    idx = 0
    while idx != (len(chunk)) :
        try:
            lexrank.summarize(chunk[idx])
            summaries = lexrank.probe(3)
        except:
            idx += 1
            continue    
        summaries[0] = summaries[0]+'. '
        summaries[1] = summaries[1]+'. '
        summaries[2] = summaries[2]+'. '

        chunk[idx] = ''.join(summaries)
        chunk2.append(chunk[idx])
        idx += 1

    chunk = []
    chunkToDB = ''
    for c in chunk2:
        chunkToDB += c + '\n'
    
    post.content = chunkToDB
    # 요약본이 아닌 원본으로 ibm Natural Language Understanding
    post.keyword, post.relevance, post.category_ibm = ibmContent(text)
    post.save()
    