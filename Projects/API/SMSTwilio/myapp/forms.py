from django import forms

class PhoneNumberForm(forms.Form):
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1234567890'})
    )

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 6-digit OTP'})
    )
