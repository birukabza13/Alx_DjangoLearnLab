from django.db import models


# Author model to store author information
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Book model to store book information
class Book(models.Model):
    title = models.CharField(max_length=500)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title



