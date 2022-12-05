from django.contrib import admin

# Register your models here.
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display=('username','email','first_name','last_name','mobile_number','address')
    search_fields=('username','email','first_name','mobile_number','address')


admin.site.register(CustomUser,CustomUserAdmin)