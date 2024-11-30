from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields of the Book model

    def validate_publication_year(self, value):
        """Ensure publication_year is not in the future."""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested BookSerializer to show related books

    class Meta:
        model = Author
        fields = ['name', 'books']  # Include name and related books

