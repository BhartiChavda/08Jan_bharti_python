from django.shortcuts import render, redirect

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'home.html')
