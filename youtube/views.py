from django.shortcuts import render, get_object_or_404,redirect
from .models import UrlTest
from .forms import UrlTestForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .yToA import youtubeToAudio
import os
import io
import sys
import wave
from pydub import AudioSegment
from pydub.utils import make_chunks
from .speechToText import *
def urlUpload(request):
    summaries = []
    url = ''
    text_list = []
    if request.method == 'POST':
        form = UrlTestForm(request.POST)
        if form.is_valid():
            lexrank = LexRank()
            ytForm = form.save()
            url = ytForm.url
            vName = youtubeToAudio(url)
            text_list = splitandSTT(vName, 'en-US')
            lexrank.summarize(text_list)
            summaries = lexrank.probe(3)  # `num_summaries` can be `None` (using auto-detected topics)
            os.remove(vName)
    else:
        form = UrlTestForm()
    return render(request, 'youtube/home.html', {
        'form': form,'text_list':text_list,
    })