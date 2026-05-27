from rest_framework import serializers
from testapp.models import *

class studserializer(serializers.ModelSerializer):
    class Meta:
        model=studmodel
        fields='__all__'