from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=10,default=None,unique=False,null=True)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
