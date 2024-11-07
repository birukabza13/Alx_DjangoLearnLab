from django.urls import path
from .views import list_books
from .views import LibraryDetailView, login_view, logout_view, register_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library', LibraryDetailView.as_view(), name="library_books"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
