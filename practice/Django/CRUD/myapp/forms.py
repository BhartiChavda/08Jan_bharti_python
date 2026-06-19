from django import forms
from .models import *

class studentforms(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"