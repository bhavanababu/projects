from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=120)
    age=models.PositiveIntegerField()
    moblie=models.PositiveIntegerField()
    email=models.EmailField()
    profile=models.ImageField(upload_to="profiles")



