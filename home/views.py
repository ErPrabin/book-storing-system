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
            print(loanbook.status)
            if(loanbook.status==0):
                update(request,loanbook)
                return redirect('/?mesg=Success')
                return render(request,'index.html',{'mesg':'Booking Success.'})
            else:
                return redirect('/?mesg=failed')
                return render(request,'index.html',{'mesg':'Booking Failed.'})
        except LoanBook.DoesNotExist :
            create(request)
            return redirect('/?mesg=Success')

            return render(request,'index.html',{'mesg':'Book Doesnot Exist.'})


        
    else :
        book=Book.objects.get(id=request.GET.get('book_id'))
        return render(request, 'booking.html',{'book':book})
def create(request):
     loadbook=LoanBook(status=1,book_id=request.POST['book_id'],user_id=request.user.id,date=request.POST['date'])
     loadbook.save()
     return True

def update(request,loanbook):
    loanbook=LoanBook.objects.update(status=1,user_id=request.user.id,date=request.POST['date'])
    return loanbook