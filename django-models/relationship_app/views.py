from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


class LoginView(LoginView):
    pass


class LogoutView(LogoutView):
    next_page = reverse_lazy("login")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def list_books(request):
    book = Book.objects.all()
    context = {"books": book}
    return render(request, "relationship_app/list_books.html", context)


def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"


def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    context = {
        'role': 'Admin',
        'message': 'Welcome, Admin!',
        'total_books': 150,  
        'total_members': 50, 
        'total_librarians': 5  
    }
    return render(request, 'admin_view.html', context)

@user_passes_test(is_librarian)
def librarian_view(request):
    context = {
        'role': 'Librarian',
        'message': 'Welcome, Librarian!',
        'assigned_books': 120,  
        'total_members': 50 
    }
    return render(request, 'librarian_view.html', context)


@user_passes_test(is_member)
def member_view(request):
    context = {
        'role': 'Member',
        'message': 'Welcome, Member!',
        'borrowed_books': 5,  
        'membership_expiration': '2024-12-31'  
    }
    return render(request, 'member_view.html', context)


