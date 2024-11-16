```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.get(id=1)

book.title = "Nineteen Eighty-Four"
print(book.title)
# expected output
Nineteen Eighty-Four
