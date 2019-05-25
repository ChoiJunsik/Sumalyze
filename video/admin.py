from django.contrib import admin
from .models import VideoPost

class VideoAdmin(admin.ModelAdmin):
    list_display = ['pk','author','title','category','lang','created',]
    raw_id_fields = ['author']
    list_filter = ['category','lang','author']
    seacrh_fields = ['title','author']
    ordering = ['-created']

admin.site.register(VideoPost,VideoAdmin)