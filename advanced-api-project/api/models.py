from django.db import models

class Author(models.Model):  # class Author model
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    

class Book(models.Model): # class Book model
    title = models.CharField(max_length=225)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    