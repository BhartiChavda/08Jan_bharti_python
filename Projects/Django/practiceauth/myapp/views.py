from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=="POST":
        em=request.POST['email']
        pa=request.POST['password']
        user= dbauth.objects.filter(email=em, password=pa)
        if user:
             print("login successfull!!!!")
             request.session["user"]=em
             return redirect('home')
        else:
            print("login faield!!!!")
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        nreq=authform(request.POST)
        if nreq.is_valid():
            nreq.save()
            print('successfully signup!!!')
            return redirect('/')
        else:
            print(nreq.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user': user})

def ulogout(request):
    logout(request)
    return redirect('/')
  


