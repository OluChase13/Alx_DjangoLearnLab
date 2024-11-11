# Create a Book Instance

To create a new Book instance with the title "1984", author "George Orwell", and publication year 1949, use the following command:

```python
from bookshelf.models import Book

# Creating the Book instance
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verifying the creation by printing
print(new_book)


1984 by George Orwell (1949)

This documents the steps and the expected output for creating a new book instance in Django using the ORM.