import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm

@login_required(login_url='login')
def home(request):
    return render(request, 'registration_app/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Store data in session to create user after OTP verify
            request.session['register_data'] = {
                'username': form.cleaned_data['username'],
                'first_name': form.cleaned_data['first_name'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password']
            }
            
            # Generate 6-digit OTP
            otp = str(random.randint(100000, 999999))
            request.session['otp'] = otp
            
            # Send OTP via Email
            user_name = form.cleaned_data['first_name']
            user_email = form.cleaned_data['email']
            
            subject = 'Your Registration OTP'
            message = f'Dear {user_name},\n\nYour OTP for registration is: {otp}\n\nRegards,\nDjango Team'
            
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [user_email],
                    fail_silently=False,
                )
                messages.info(request, 'An OTP has been sent to your email. Please verify to complete registration.')
                return redirect('otp_verify')
            except Exception as e:
                messages.error(request, f'Failed to send OTP. Error: {str(e)}')
                return redirect('register')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration_app/register.html', {'form': form})

def otp_verify(request):
    if 'register_data' not in request.session or 'otp' not in request.session:
        messages.error(request, 'Session expired. Please register again.')
        return redirect('register')

    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')
        
        if user_otp == session_otp:
            # OTP matched, create user
            data = request.session['register_data']
            user = User(
                username=data['username'],
                first_name=data['first_name'],
                email=data['email']
            )
            user.set_password(data['password'])
            user.save()
            
            # Clear session
            del request.session['register_data']
            del request.session['otp']
            
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            
    return render(request, 'registration_app/otp_verify.html')

def user_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        
        # Try to find the user's actual username if they entered an email address
        user_obj = User.objects.filter(email=username_or_email).first()
        if user_obj:
            username_to_auth = user_obj.username
        else:
            username_to_auth = username_or_email # Fallback, assume they entered their username
            
        # Authenticate using the username
        user = authenticate(request, username=username_to_auth, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {user.first_name}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            
    return render(request, 'registration_app/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')
