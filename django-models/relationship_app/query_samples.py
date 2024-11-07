from .models import Book, Library, Librarian


# Query all books by a specific author.
books = Book.objects.get(author="author_name")

# List all books in a library.
library = Library.objects.get(name="library_name")
books = library.books.all()

# Retrieve the librarian for a library.
library = Librarian.objects.get(library="library_name")
 


