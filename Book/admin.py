from Book.models import Book
from django.contrib import admin

class BookAdmin(admin.ModelAdmin):
    list_display=('name','author','publisher','year')
    search_fields=('name','author','publisher')

# Register your models here.
admin.site.register(Book,BookAdmin)
