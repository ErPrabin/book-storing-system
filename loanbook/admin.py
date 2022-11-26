from loanbook.models import LoanBook
from django.contrib import admin

class LoadBookAdmin(admin.ModelAdmin):
    list_display=('book','user','status','created_at')
    search_fields=['book__name','book__author','user__username','user__email','status']
    

# Register your models here.
admin.site.register(LoanBook,LoadBookAdmin)
