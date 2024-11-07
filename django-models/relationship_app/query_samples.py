from .models import Book, Library


# Query all books by a specific author.
books = Book.objects.get(author="#author_name")

# List all books in a library.
library = Library.objects.get(name="#library_name")
books = library.books.all()

# Retrieve the librarian for a library.
library = Library.objects.get(name="#Library")
librarian = library.librarian  


