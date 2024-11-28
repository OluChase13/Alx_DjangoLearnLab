from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # Serializes all the fields in Book model

    def validate_publication_year(self, value): # Custom validation to ensure publication_year is not in the future
        if value > date.today().year:
            raise serializers.ValidationError("Publication year can not be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) # Nested serializer for books
    class Meta:
        model = Author
        fields = ['id', 'name', 'books'] # Includes Book serializer to display all author's books

