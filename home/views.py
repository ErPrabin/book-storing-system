from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from Book.models import Book
from django.core.paginator import Paginator
from loanbook.models import LoanBook
from django.http import JsonResponse
from django.contrib import messages
import json

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    # if request.method == 'POST':
    #     return 'hello'
    books= Book.objects.all().prefetch_related('user')
    paginator = Paginator(books, 10) # Show 2 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'books': page_obj})

    return render(request, 'index.html',{'books':books})

def booking(request):
    if request.method=='POST':
        try:
            loanbook=LoanBook.objects.get(book_id=request.POST['book_id'])
            if(loanbook.status==0):
                update(request,loanbook)
                messages.success(request, 'Booking Success')
                return redirect('/')
                return render(request,'index.html',{'mesg':'Booking Success.'})
            else:
                messages.error(request, 'Booking Failed')
                return redirect('/')
                return render(request,'index.html',{'mesg':'Booking Failed.'})
        except LoanBook.DoesNotExist :
            create(request)
            messages.success(request, 'Booking Success')
            return redirect('/')

            return render(request,'index.html',{'mesg':'Book Doesnot Exist.'})


        
    else :
        book=Book.objects.get(id=request.GET.get('book_id'))
        return render(request, 'booking.html',{'book':book})
def create(request):
     loadbook=LoanBook(status=1,book_id=request.POST['book_id'],user_id=request.user.id,date=request.POST['date'])
     loadbook.save()
     return True

def update(request,loanbook):
    loanbook.status=1
    loanbook.user_id=request.user.id
    loanbook.date=request.POST['date']
    loanbook.save()
    # loanbook=LoanBook.objects.update(status=1,user_id=request.user.id,date=request.POST['date'])
    return loanbook

def myBook(request):
    books=Book.objects.filter(loanbook__status=1,loanbook__user_id=request.user.id)
    paginator = Paginator(books, 10) # Show 2 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mybook.html',{'books':page_obj})

def releaseBook(request,id):
    loanbook=LoanBook.objects.get(pk=id)

    try:
        loanbook.status=0
        loanbook.date=None
        loanbook.save()
        messages.success(request, 'Book Released.')
        return redirect('/my-book')
        
    except Book.DoesNotExist :
        messages.error(request, 'Book Doesnot Exist.')
        return redirect('/my-book')

def addBook(request):
    if request.method=="POST":
        book=Book(name=request.POST['name'],author=request.POST['author'],publisher=request.POST['publisher'],book_type=request.POST['book_type'],year=request.POST['year'],user=request.user)
        book.save()
        messages.success(request, 'Book Added.')
        return redirect('/')
    else:
        return render(request,'addbook.html')
def myBookList(request):
    books=Book.objects.filter(user_id=request.user.id)
    paginator = Paginator(books, 10) # Show 2 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'mybooklist.html',{'books':page_obj})
