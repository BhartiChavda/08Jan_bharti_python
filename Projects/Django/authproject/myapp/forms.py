from django import forms
from .models import *

class authform(forms.ModelForm):
    class Meta:
        model=authuser
        fields='__all__'