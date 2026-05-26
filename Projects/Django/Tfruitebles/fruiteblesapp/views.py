from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')
def errorpage(request):
    return render(request,'errorpage.html')
def shop(request):
    return render(request,'shop.html')
def shopdetail(request):
    return render(request,'shopdetail.html')
def testimonial(request):
    return render(request,'testimonial.html')
