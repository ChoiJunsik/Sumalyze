from django.shortcuts import render, get_object_or_404,redirect
from .models import PdfPost
from .forms import PdfPostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .tasks import pdfSumalyze
from django.conf import settings

import os,re

def index(request):
    if request.method == 'POST':
        form = PdfPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = PdfPost()
            post.author = request.user
            post.category = form.cleaned_data['category']
            post.pdf = request.FILES['pdf']
            post.lang = form.cleaned_data['lang']
            post.title = form.cleaned_data['title']#re.sub('[^가-힣\\s]', '', str(post.pdf))
            post.created = timezone.now()
            post.save()
            pdfSumalyze.delay(post.pk)
            return render(request, 'pdf/pdf.html', {
            'success': True,
            })
    else:
        form = PdfPostForm()
    return render(request, 'pdf/pdf.html', {
          'form': form,
    })