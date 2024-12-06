from .views import (
    UserLoginView,
    UserLogoutView,
    UserRegisterView,
    UserProfileView
)
from django.urls import path

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("profile/", UserProfileView.as_view(), name="profile_page")
]


