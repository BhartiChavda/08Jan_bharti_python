from django.shortcuts import render
import random
# Create your views here.
counter= 0
def index(request):
    global counter 
    counter += 1
    name=""
    if request.method=="POST":
        name=request.POST.get('username')
    
    num=random.randint(1111,9999)
    return render(request, 'index.html', {
        'name': name, 
        'num': num, 
        'counter': counter
        })

    