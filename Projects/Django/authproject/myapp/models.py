from django.db import models

# Create your models here.
class authuser(models.Model):
    
        fullname=models.CharField(max_length=20)
        email=models.EmailField()
        password=models.CharField(max_length=20)
        cpassword=models.CharField(max_length=20)
