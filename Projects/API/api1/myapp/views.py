from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

"""@api_view(["GET"])
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
            return Response(status=status.HTTP_400_BAD_REQUEST)"""
        


#--------#---------#----------#-----------#----------#-
#2nd try
#fetch all data 
@api_view(['GET'])
def data(request):
    obj2=apimodels.objects.all()
    obj3=apiserializer(obj2,many=True)
    return Response(obj3.data)

#fetch specified data
@api_view(['GET'])
def specified(request,id):
    try:
        obj4=apimodels.objects.get(id=id)
    except apimodels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        obj5=apiserializer(obj4)
        return Response(obj5.data)
#insert data   
@api_view(['POST'])    
def cr(request):
    if request.method=="POST":
        obj6=apiserializer(data=request.data)
        if obj6.is_valid():
            obj6.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
#delete data 
@api_view(['DELETE'])       
def de(request,id):
    try:
        obj7=apimodels.objects.get(id=id)
    except apimodels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="DELETE":
        obj7.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

#update data
@api_view(['PUT','GET'])
def up(request,id):
    try:
        obj8=apimodels.objects.get(id=id)
    except apimodels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="PUT":
        obj9=apiserializer(data=request.data,instance=obj8)
        if obj9.is_valid():
            obj9.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    



       
