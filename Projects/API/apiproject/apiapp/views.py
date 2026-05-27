from django.shortcuts import render
from .serialize import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def apidata(request):
    stud=student_info.objects.all()
    serial=studserializers(stud,many=True)
    return Response(serial.data)