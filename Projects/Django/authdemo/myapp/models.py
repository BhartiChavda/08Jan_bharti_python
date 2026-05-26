from django.db import models

# Create your models here.

class dmodel(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)