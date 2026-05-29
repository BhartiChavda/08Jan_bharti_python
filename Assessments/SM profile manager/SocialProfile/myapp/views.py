from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm
import csv

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'myapp/profile_list.html', {'profiles': profiles})

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'myapp/profile_form.html', {'form': form})

def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'myapp/profile_form.html', {'form': form})

import os
from django.conf import settings

def export_profiles_csv(request):
    file_path = os.path.join(settings.BASE_DIR, 'profiles_export.csv')
    
    # Using Context Manager as required by the assessment
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Bio', 'Social Link'])
        
        profiles = Profile.objects.all().values_list('id', 'first_name', 'last_name', 'email', 'bio', 'social_link')
        for profile in profiles:
            writer.writerow(profile)
            
    # Serve the file
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="profiles.csv"'
        
    return response

