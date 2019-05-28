from __future__ import absolute_import
from sumalyze.celery import app
from celery import shared_task
from django.shortcuts import render, get_object_or_404,redirect
import os
import io
import sys
import wave
import re
from .models import AudioPost
from video.speechToText import *
from sumalyze.ibmContent import ibmContent
from sumalyze.ibmIndex import ibmIndex
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\media\\'

@shared_task
def audioSumalyze(pk):
    post = get_object_or_404(AudioPost, pk=pk)
    lang = 'en-US'    
    if post.lang == '한국어':
        lang = 'ko-KR'
    from lexrankr import LexRank
    lexrank = LexRank()
    chunk2 = []
    chunk =[] 
    
    #speechtotext(str(post.pdf), lang, chunk)
    chunk = splitandSTT(path+str(post.pdf), lang)
    text = " ".join(chunk)
    idxToDB = ''
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
        indexStr = ''.join(summaries)
        chunk[idx] = indexStr
        idxToDB += ibmIndex(indexStr,summaries)
        idxToDB += '#'
        chunk2.append(chunk[idx])
        idx += 1
    post.index = idxToDB


    chunk = []
    chunkToDB = ''
    for c in chunk2:
        chunkToDB += c + '\n'
    
    post.content = chunkToDB
    # 요약본이 아닌 원본으로 ibm Natural Language Understanding
    post.keyword, post.relevance, post.category_ibm = ibmContent(text)
    post.save()
