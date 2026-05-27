from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Doctor, Patient
from .forms import DoctorForm, PatientRegistrationForm
import json
from django.contrib.auth.decorators import login_required

# Lab 1: Render HTML Welcome
def home(request):
    return render(request, 'doctor/home.html')

# Lab 2: Display webpage with custom CSS styling for a doctor profile page
def doctor_profile(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'doctor/profile.html', {'doctor': doctor})

# Lab 9, 12: List all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})

def contact(request):
    return render(request, 'doctor/contact.html')

# Lab 3, 10: JS-enabled form validation for patient registration
def patient_registration(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientRegistrationForm()
    return render(request, 'doctor/registration.html', {'form': form})

# Lab 14: AJAX CRUD Operations
def doctor_ajax_list(request):
    doctors = list(Doctor.objects.values('id', 'name', 'specialty', 'availability', 'location'))
    return JsonResponse({'doctors': doctors})

def doctor_ajax_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        doctor = Doctor.objects.create(
            name=data['name'],
            specialty=data['specialty'],
            availability=data.get('availability', ''),
            location=data.get('location', '')
        )
        return JsonResponse({'id': doctor.id, 'status': 'success'})

def doctor_ajax_delete(request, doctor_id):
    if request.method == 'DELETE':
        doctor = get_object_or_404(Doctor, id=doctor_id)
        doctor.delete()
        return JsonResponse({'status': 'deleted'})

# Lab 16: Paytm Payment dummy view
def payment(request):
    return render(request, 'doctor/payment.html')

# Lab 20: Google Maps view
def map_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/map.html', {'doctors': doctors})
