from django.shortcuts import render, redirect
from .forms import *

def index(request):
    if request.method=='POST':
        form = studform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request,'index.html')


def showdata(request):
    dataa = student_info.objects.all()
    return render(request,'showdata.html',{'data':dataa})

def deletedata(request,id):
    obj = student_info.objects.get(id=id)
    student_info.delete(obj)
    return redirect("showdata")

def updatedata(request,id):
    obj = student_info.objects.get(id=id)
    if request.method=='POST':
        form = studform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showdata')
        else:
            print(form.errors)
    return render(request,'updatedata.html',{'obj': obj})


    