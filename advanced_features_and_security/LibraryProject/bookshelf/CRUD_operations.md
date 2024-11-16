<!-- create -->
```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title = "1984", author = "George Orwell", publication_year="1949")

# Output the book to confirm creation
book

<Book: Book object (1)>

# retrieve


# Create a Book instance
book = Book.objects.get(id=1)

print(book.title, book.author, book.publication_year)
# expected output
1984, George Orwell, 1949

# update



# Create a Book instance
book = Book.objects.get(id=1)

book.title = "Nineteen Eighty-Four"
print(book.title)
# expected output
Nineteen Eighty-Four

# delete

# Create a Book instance
book = Book.objects.get(id=1)

book.delete()

books = Book.objects.all()

print(books)

# expected output
<QuerySet []>

