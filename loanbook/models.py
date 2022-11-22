from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from Book.models import Book

from accounts.models import User


# Create your models here.
class LoanBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.BooleanField(default=None, blank=True, null=True)
    date=models.DateField(default=None, blank=True, null=True)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateField(default=timezone.now)


    # def __str__(self):
    #     return self.name

