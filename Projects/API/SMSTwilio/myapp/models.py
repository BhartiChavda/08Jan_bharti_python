from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"


class OTPVerification(models.Model):
    phone_number = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_expired(self):
        # 5 minutes expiration
        now = timezone.now()
        diff = now - self.created_at
        return diff.total_seconds() > 300

    def __str__(self):
        return f"{self.phone_number} - {self.otp}"
