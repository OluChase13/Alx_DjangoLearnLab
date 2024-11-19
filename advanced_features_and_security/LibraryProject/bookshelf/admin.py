from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Book, CustomUser, Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Filters to allow quick sorting and categorization
    list_filter = ('publication_year', 'author')

    # Search capability by title and author
    search_fields = ('title', 'author')

#registering the new CustomUserModel
admin.site.register(CustomUser, UserAdmin)