from django import forms
from .models import UrlTest

class UrlTestForm(forms.ModelForm):

    class Meta:
        model = UrlTest
        fields = ('title', 'url')
