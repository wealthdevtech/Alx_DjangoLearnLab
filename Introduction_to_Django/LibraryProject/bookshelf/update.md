book.title
x = Book.objects.all()[0]
>>> x.title
'1984'
>>> x.title = 'Nineteen Eighty-Four'
>>> x.save()
>>> x.title
'Nineteen Eighty-Four'
Book.objects.all().values()[0]
{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}
