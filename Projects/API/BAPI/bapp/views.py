from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    return render(request,'index.html')

@api_view(['GET'])
def fetchdata(request):
    obj1=studentm.objects.all()
    serializer=studserial(obj1, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def getdata(request,id):
    try:
        studid=studentm.objects.get(id=id)
    except studentm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serial=studserial(data=request.data)
