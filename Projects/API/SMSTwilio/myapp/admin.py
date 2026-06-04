from django.contrib import admin
from .models import UserProfile, OTPVerification

admin.site.register(UserProfile)
admin.site.register(OTPVerification)

