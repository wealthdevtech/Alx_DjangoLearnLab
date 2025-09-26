from django.shortcuts import render, loader
from django.http import HttpResponse
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required

# Create your views here.
def list_books(request):
    template = loader.get_template('relationship_app/list_books.html')
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return HttpResponse(template.render(template, context))

class library_detailView(ListView):
    model = ListView
    template_name = 'relationship_app/library_detail.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['object_list']  # Optional, if you want a custom name
        context['name'] = 'All Available Books'
        return context

 "relationship_app.can_add_book", "relationship_app.can_change_book", "relationship_app.can_delete_book"

