from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        em=request.POST['email']
        pa=request.POST['password']
        user=dmodel.objects.filter(email=em,password=pa)
        if user:
            print("login successfully!!!")
            return redirect('home')
        else:
            print("try again!!!!!")        
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        objs=dform(request.POST)
        if objs.is_valid():
            objs.save()
            return redirect('/')
        else:
            print(objs.errors)
            
    return render(request,'signup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')


