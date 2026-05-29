from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = UserProfileForm()
        
    profiles = UserProfile.objects.all()
    return render(request, 'myapp/profile_view.html', {'form': form, 'profiles': profiles})
