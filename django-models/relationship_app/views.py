from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


def list_books(request):
    book = Book.objects.all()
    context = {"books": book}
    return render(request, "relationship_app/list_books.html", context)
