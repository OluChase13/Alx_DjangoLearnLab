from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Filters to allow quick sorting and categorization
    list_filter = ('publication_year', 'author')

    # Search capability by title and author
    search_fields = ('title', 'author')

