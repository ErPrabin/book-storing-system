from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,default=None)
    mobile_number=models.CharField(max_length=10)
    email=models.EmailField(max_length=50,unique=True)
    address=models.CharField(max_length=100)

    objects =CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
