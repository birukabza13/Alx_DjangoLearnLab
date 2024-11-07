from django.urls import path
from .views import list_books
from .views import LibraryDetailView, LoginView, LogoutView, RegisterView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library', LibraryDetailView.as_view(), name="library_books"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
] 
