from django.shortcuts import render, get_object_or_404,redirect
from .models import TextPost
from .forms import TextPostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .tasks import textSumalyze
from django.conf import settings

import os,re

def index(request):
    if request.method == 'POST':
        form = TextPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = TextPost()
            post.author = request.user
            post.category = form.cleaned_data['category']
            post.text = request.POST['text']
            post.lang = form.cleaned_data['lang']
            post.title = form.cleaned_data['title']
            post.created = timezone.now()
            post.save()
            textSumalyze.delay(post.pk)
            return render(request, 'text/text.html', {
            'success': True,
            })
    else:
        form = TextPostForm()
    return render(request, 'text/text.html', {
          'form': form,
    })