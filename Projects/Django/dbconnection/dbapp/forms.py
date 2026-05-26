from django import forms
from .models import *

class studform(forms.ModelForm):
    class Meta:
        model = student_info
        fields = '__all__'  
        