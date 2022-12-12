from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

from accounts.models import CustomUser


# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    book_type=models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateField(default=timezone.now)


    def __str__(self):
        return self.name

