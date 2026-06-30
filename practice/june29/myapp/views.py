from django.shortcuts import render,redirect
from .forms import *
from .models import *


# Create your views here.

def index(request):
    if request.method=="POST":
        form=studforms(request.POST)
        if form.is_valid():
            form.save()
            print("data insert successfully!")
        else:
            print(form.errors)
    return render(request, 'index.html')

def showdata(request):
    data=studmodel.objects.all()
    return render(request,'showdata.html',{'data': data})

def update(request,id):
    pass

    
