from django.urls import path
from .views import list_books
from .views import LibraryDetailView, LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library", LibraryDetailView.as_view(), name="library_books"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
]
