from __future__ import absolute_import
from sumalyze.celery import app
from celery import shared_task
from .models import PdfPost
from .pdfToText import convert_pdf_to_txt
from sumalyze.ibmContent import ibmContent
from sumalyze.ibmIndex import ibmIndex
from django.shortcuts import render, get_object_or_404,redirect
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

@shared_task
def pdfSumalyze(pk):
    post = get_object_or_404(PdfPost, pk=pk)
    from lexrankr import LexRank
    lexrank = LexRank()
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\media\\'+str(post.pdf)
    text = convert_pdf_to_txt(path)
    os.remove(path)

    chunk =[]
    if len(text) < 650:
        chunk.append(text)
    else: 
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
    post.pdf = None
    post.index = idxToDB
    # 요약본이 아닌 원본으로 ibm Natural Language Understanding
    post.keyword, post.relevance, post.category_ibm = ibmContent(text)
    post.save()

