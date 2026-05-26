from django import forms
from .models import *


class authform(forms.ModelForm):
    class Meta:
        model=dbauth
        fields="__all__"