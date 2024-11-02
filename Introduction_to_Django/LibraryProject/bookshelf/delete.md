```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.get(id=1)

book.delete()

books = Book.objects.all()

print(books)

# expected output
<QuerySet []>