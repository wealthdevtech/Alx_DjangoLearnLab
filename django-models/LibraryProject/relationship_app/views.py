from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import ListView

# Create your views here.
def list_books(request):
    template = loader.get_template('list_books.html')
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return HttpResponse(template.render(template, context))

class library_detailView(ListView):
    model = ListView
    template_name = 'templates/library_detail.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['object_list']  # Optional, if you want a custom name
        context['name'] = 'All Available Books'
        return context