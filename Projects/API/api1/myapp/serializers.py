from rest_framework import serializers
from .models import *

class apiserializer(serializers.ModelSerializer):
    class Meta:
        model=apimodels
        fields="__all__"
