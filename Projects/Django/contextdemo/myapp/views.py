from django.shortcuts import render
import random

# Create your views here.

count=0
def index(request):
    global count
    name="bharti"
    num=random.randint(1111,9999)
    count += 1
    return render(request,'index.html',{'name':name, 'num':num, 'count':count})
