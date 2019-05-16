from django import forms
from .models import *

class musicForm(forms.ModelForm):
    class Meta:
        model = Music
        exclude = ['']