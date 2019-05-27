from django import forms
from .models import PdfPost

class PdfPostForm(forms.ModelForm):

    class Meta:
        model = PdfPost
        fields = ('pdf', 'category','lang', 'title')
