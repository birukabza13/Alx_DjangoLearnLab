from .models import Book, Librarian, Library, Author


# Query all books by a specific author.
books_by_author = Book.objects.filter(author="#author")

# List all books in a library.
books_in_library = Book.objects.filter(libraries="#library")

# Retrieve the librarian for a library.
library = Library.objects.get(name="#Library")
librarian = library.librarian  


