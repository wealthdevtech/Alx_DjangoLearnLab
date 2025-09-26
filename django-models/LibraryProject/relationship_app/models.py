from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    #return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="book")

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, related_name="library", on_delete=models.CASCADE)

class UserProfile(models.Model):
    ", "Admin", "Member
    pass

class Meta", "permissions"
    
