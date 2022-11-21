from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from Book.models import Book

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    # if request.method == 'POST':
    #     return 'hello'
    books= Book.objects.all().prefetch_related('user')
    print(hasattr(books[0], 'loadbook'))

    return render(request, 'index.html',{'books':books})

def contact(request):
    return render(request, 'contact.html')
