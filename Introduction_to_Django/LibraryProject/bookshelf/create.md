book1 = Book(title = '1984', author = 'George Orwell', publication_year = 1949)
book1.save()
"""Book.objects.all().values()[0]
{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}"""