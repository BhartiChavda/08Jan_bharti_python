from django.db import models

# Create your models here.

class dbauth(models.Model):
  
        fullname=models.CharField(max_length=20)
        email=models.EmailField()
        password=models.CharField(max_length=20)
        cpassword=models.CharField(max_length=20)
