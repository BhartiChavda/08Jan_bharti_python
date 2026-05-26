from django.db import models

# Create your models here.

class student_info(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateTimeField()
    mobile=models.BigIntegerField()
    address=models.TextField()

