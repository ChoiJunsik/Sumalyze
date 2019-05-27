from django import forms
from .models import AudioPost

class AudioPostForm(forms.ModelForm):

    class Meta:
        model = AudioPost
        fields = ('pdf', 'category','lang', 'title')
