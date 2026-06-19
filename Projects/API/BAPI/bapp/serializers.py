from rest_framework import serializers
from .models import *

class studserial(serializers.ModelSerializer):
    class Meta:
        model=studentm
        fields='__all__'