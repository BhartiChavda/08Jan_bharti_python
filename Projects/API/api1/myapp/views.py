from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(["GET"])
def apidata(request):
    obj1=apimodels.objects.all()
    obj2=apiserializer(obj1,many=True)
    return Response(obj2.data)

@api_view(['GET'])
def apiget(request,id):
    try:
        stid=apimodels.objects.get(id=id)
    except apimodels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serial=apiserializer(stid)
        return Response(data=serial.data)

@api_view(['POST'])  
def apipost(request):
    if request.method=="POST":
        serial=apiserializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def apidelete(request,id):
    try:
        stid=apimodels.objects.get(id=id)
    except apimodels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="DELETE":
        stid.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['PUT'])
def apiupdate(request,id):
    try:
        stid=apimodels.objects.get(id=id)
    except apimodels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="PUT":
        serial=apiserializer(data=request.data,instance=stid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
