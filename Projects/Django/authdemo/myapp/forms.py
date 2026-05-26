from django import forms
from .models import *


class dform(forms.ModelForm):
    class Meta:
        model=dmodel
        fields='__all__'