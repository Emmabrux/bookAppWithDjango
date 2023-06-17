from django.shortcuts import render
from bookstore.models import Book
# Create your views here.


def index(request):
    #here is the content for the index function..
    content_value="welcome to our homepage"
    return render(request,'index.html',{'content_key':content_value})
   
def login(request):
    return render(request, 'login.html',{})   

def landing(request):
    #Fetching all books using Object related mapping (ORM)
    Books_value=Book.objects.all()
    return render(request, 'landing.html',{'book_key':Books_value})

def register(request):
    #Fetching all books using Object related mapping (ORM)
    Books_value=Book.objects.all()
    return render(request, 'register.html',{'book_key':Books_value})

def groups(request):
    #Fetching all books using Object related mapping (ORM)
    Books_value=Book.objects.all()
    return render(request, 'groups.html',{'book_key':Books_value})

def events(request):
    #Fetching all books using Object related mapping (ORM)
    Books_value=Book.objects.all()
    return render(request, 'events.html',{'book_key':Books_value})

def event(request):
    return render(request,'event.html',{})