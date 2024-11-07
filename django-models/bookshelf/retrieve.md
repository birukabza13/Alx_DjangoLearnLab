```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.get(id=1)

print(book.title, book.author, book.publication_year)
# expected output
1984, George Orwell, 1949
