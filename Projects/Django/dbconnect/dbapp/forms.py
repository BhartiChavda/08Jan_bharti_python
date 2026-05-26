from django import forms
from .models import *

class studforms(forms.ModelForm):
    class Meta:
        model=database
        fields='__all__'