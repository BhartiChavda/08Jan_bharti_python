from django import forms
from .models import *

class studforms(forms.ModelForm):
    class Meta:
        model= studmodel
        fields='__all__'