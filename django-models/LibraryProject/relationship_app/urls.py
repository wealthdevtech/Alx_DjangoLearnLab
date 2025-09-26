from django.urls import path
from .views import list_books, library_detailView

urlpatterns = [
    path('list_books/', views.list_books, name="list_books"),
    path('library_detail/', library_detailView.as_view(), name='library_detail'),
]