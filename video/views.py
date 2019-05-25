from django.shortcuts import render, get_object_or_404,redirect
from .models import VideoPost
from .forms import VideoPostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .tasks import videoSumalyze
import re
def index(request):
    if request.method == 'POST':
        form = VideoPostForm(request.POST)
        if form.is_valid():
            post = VideoPost()
            post.author = request.user
            post.category = form.cleaned_data['category']
            post.url = request.POST['url']
            post.lang = form.cleaned_data['lang']
            post.created = timezone.now()
            post.save()
            videoSumalyze.delay(post.pk)
            return render(request, 'video/video.html', {
            'success': True,
            })
    else:
        form = VideoPostForm()
    return render(request, 'video/video.html', {
        'form': form,
    })