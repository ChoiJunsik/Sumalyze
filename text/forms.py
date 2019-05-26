from django import forms
from .models import TextPost

class TextPostForm(forms.ModelForm):

    class Meta:
        model = TextPost
        fields = ('text', 'category','lang')
