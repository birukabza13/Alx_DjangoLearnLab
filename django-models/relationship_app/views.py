from django.shortcuts import render
from .models import Book

def list_books(request):
    book = Book.objects.all()

    context = {
        "books": book
    }

    return render(request, 'relationship_app/book_list.html', context)

