from django.contrib import admin
from .models import TextPost

class TextAdmin(admin.ModelAdmin):
    list_display = ['pk','author','title','category','lang','created',]
    raw_id_fields = ['author']
    list_filter = ['category','lang','author']
    seacrh_fields = ['title','author']
    ordering = ['-created']

admin.site.register(TextPost,TextAdmin)