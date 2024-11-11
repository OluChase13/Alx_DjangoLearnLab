from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return None


# List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()  # Returns all books related to the library
    except Library.DoesNotExist:
        return None


# Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Librarian.objects.get(library=library_name)
        return Librarian.library  # Returns the librarian related to the library
    except Library.DoesNotExist:
        return None
