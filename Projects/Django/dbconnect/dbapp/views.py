from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):
    if request.method=="POST":
        form=studforms(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request,'index.html')

def showdata(request):
    sdata=database.objects.all()
    return render(request,'showdata.html',{'sdata':sdata})

def delete(request):
    sdata=database.objects.delete()
    return render(request,'showdata.html',{'sdata':sdata})


