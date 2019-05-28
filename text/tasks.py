from __future__ import absolute_import
from sumalyze.celery import app
from celery import shared_task
from .models import TextPost
from sumalyze.ibmContent import ibmContent
from sumalyze.ibmIndex import ibmIndex

from django.shortcuts import render, get_object_or_404,redirect
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

@shared_task
def textSumalyze(pk):
    post = get_object_or_404(TextPost, pk=pk)
    from lexrankr import LexRank
    lexrank = LexRank()
    text = post.text
    chunk = list(map(''.join, zip(*[iter(text)]*650)))
    chunk2 = []
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
    post.text = 'clear'
    # 요약본이 아닌 원본으로 ibm Natural Language Understanding
    post.keyword, post.relevance, post.category_ibm = ibmContent(text)
    post.save()

