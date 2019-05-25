from django.shortcuts import render, get_object_or_404,redirect
from .models import AudioPost
from .forms import AudioPostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .tasks import audioSumalyze
from django.conf import settings
import os,re

def index(request):
    if request.method == 'POST':
        form = AudioPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = AudioPost()
            post.author = request.user
            post.category = form.cleaned_data['category']
            post.pdf = request.FILES['pdf']
            post.lang = form.cleaned_data['lang']
            post.title = re.sub('[^가-힣\\s]', '', str(post.pdf))
            post.created = timezone.now()
            post.save()
            audioSumalyze.delay(post.pk)
            return render(request, 'audio/audio.html', {
            'success': True,
            })
    else:
        form = AudioPostForm()
    return render(request, 'audio/audio.html', {
          'form': form,
    })