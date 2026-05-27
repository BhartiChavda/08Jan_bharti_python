from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apidata(request):
    data=studmodel.objects.all()
    serializer=studserializer(data,many=True)
    return Response(serializer.data)