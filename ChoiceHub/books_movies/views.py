from django.shortcuts import render
import requests
from .forms import QuizForm
from .models import Book

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

# books/views.py
from .models import Book

# View to display all books in the database
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books_movies/book_list.html', {'books': books})
