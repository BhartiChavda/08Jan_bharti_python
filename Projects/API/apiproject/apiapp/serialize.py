from rest_framework import serializers
from .models import *

class studserializers(serializers.ModelSerializer):
    class Meta:
        model = student_info
        fields = '__all__' 