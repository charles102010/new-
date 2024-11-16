from django.db import models

# Create your models here.

class student(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    PhoneNo=models.CharField(max_length=13)
    Age=models.CharField(max_length=2)
    Address=models.CharField(max_length=50)