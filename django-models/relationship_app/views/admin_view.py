from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == "Admin"

@user_passes_test(is_admin)
def Admin(request):
    return render(request)