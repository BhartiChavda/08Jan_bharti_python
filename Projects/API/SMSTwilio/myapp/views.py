import random
import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from .forms import PhoneNumberForm, OTPVerificationForm
from .models import OTPVerification, UserProfile

logger = logging.getLogger(__name__)

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_view(request):
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            
            # Check if the phone number is registered
            if not UserProfile.objects.filter(phone_number=phone_number).exists():
                messages.error(request, 'This mobile number is not registered in our system.')
                return render(request, 'myapp/send_otp.html', {'form': form})

            otp = generate_otp()
            
            # Save OTP to DB
            OTPVerification.objects.create(phone_number=phone_number, otp=otp)
            
            # Send SMS via Twilio
            try:
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                    body=f'Your verification code is: {otp}. It expires in 5 minutes.',
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to=phone_number
                )
                request.session['verification_phone'] = phone_number
                messages.success(request, 'OTP sent successfully.')
                return redirect('verify_otp')
            except TwilioRestException as e:
                logger.error(f"Twilio error: {e}")
                messages.error(request, f'Twilio Error: {e.msg}')
            except Exception as e:
                logger.error(f"Error sending OTP: {e}")
                messages.error(request, 'An unexpected error occurred.')
    else:
        form = PhoneNumberForm()
    
    return render(request, 'myapp/send_otp.html', {'form': form})

def verify_otp_view(request):
    phone_number = request.session.get('verification_phone')
    if not phone_number:
        messages.error(request, 'No phone number found. Please request a new OTP.')
        return redirect('send_otp')

    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp_entered = form.cleaned_data['otp']
            
            try:
                verification = OTPVerification.objects.filter(
                    phone_number=phone_number, 
                    is_verified=False
                ).latest('created_at')
                
                if verification.is_expired():
                    messages.error(request, 'OTP has expired. Please request a new one.')
                    return redirect('send_otp')
                    
                if verification.otp == otp_entered:
                    verification.is_verified = True
                    verification.save()
                    
                    # Clear session
                    del request.session['verification_phone']
                    messages.success(request, 'Phone number verified successfully!')
                    return render(request, 'myapp/success.html')
                else:
                    messages.error(request, 'Invalid OTP. Please try again.')
            except OTPVerification.DoesNotExist:
                messages.error(request, 'No active OTP found. Please request a new one.')
    else:
        form = OTPVerificationForm()
        
    return render(request, 'myapp/verify_otp.html', {'form': form, 'phone_number': phone_number})
