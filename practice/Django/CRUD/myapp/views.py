from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method=="POST":
        form=studentforms(request.POST)
        if form.is_valid():
            form.save()
            print("insert successfully")
        else:
            print(form.errors)
            print("form is not valid")
    return render(request,'index.html')

def showdata(request):
    data=student.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    data=student.objects.get(id=id)
    if request.method=="POST":
        form=studentforms(request.POST,instance=data)
        if form.is_valid():
            form.save()
            print("update successfully")
            return redirect('showdata')
        else:
            print(form.errors)
            print("form is not valid")
    return render(request,'updatedata.html',{'data':data})