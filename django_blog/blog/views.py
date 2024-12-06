from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterView(CreateView):
    template_name = "blog/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    template_name = "blog/login.html"


class UserLogoutView(LogoutView):
    template_name = "blog/logout.html"


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "blog/profile.html"
    model = User
    form_class = UserChangeForm
    success_url = reverse_lazy("profile")

    def get_object(self, queryset=None):
        return self.request.user
    
    def post(self, request, *args, **kwargs):
            if request.method == "POST":
                form = self.get_form()
                if form.is_valid():
                    form.save()
                    return self.form_valid(form)
                else:
                    return self.form_invalid(form)
            return super().post(request, *args, **kwargs)
