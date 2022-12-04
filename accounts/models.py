import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class User(AbstractUser):
    mobile_number=models.CharField(max_length=10)
    email=models.EmailField(max_length=50,unique=True)
    address=models.CharField(max_length=100)

    objects =UserManager()

    USERNAME_FIELD: 'email'

    # def __str__(self):
    #     return self.email
