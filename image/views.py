from django.shortcuts import render, get_object_or_404,redirect
from .models import ImagePost
from .forms import ImagePostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .tasks import imageSumalyze
from django.conf import settings

import os,re

def index(request):
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = ImagePost()
            post.author = request.user
            post.category = form.cleaned_data['category']
            post.pdf = request.FILES['pdf']
            post.lang = form.cleaned_data['lang']
            post.title = form.cleaned_data['title']#re.sub('[^가-힣\\s]', '', str(post.pdf))
            post.created = timezone.now()
            post.save()
            imageSumalyze.delay(post.pk)
            return render(request, 'image/image.html', {
            'success': True,
            })
    else:
        form = ImagePostForm()
    return render(request, 'image/image.html', {
          'form': form,
    })