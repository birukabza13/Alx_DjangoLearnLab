```python
from bookshelf.models import Book

# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()  

# Output the book to confirm creation
book

<Book: Book object (1)>