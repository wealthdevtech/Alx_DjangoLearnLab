from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField(max_length=100)
    author = models.ForeignKey(Author)