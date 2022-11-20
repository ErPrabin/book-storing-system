import email
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    mobile_number=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)

    USERNAME_FIELD: 'email'
