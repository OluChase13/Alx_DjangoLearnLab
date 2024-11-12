from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from .models import UserProfile

def is_admin(user):
    # Check if the user has an associated UserProfile with role 'Admin'
    try:
        return user.userprofile.role == 'Admin'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_admin)
def admin_view(request):
    # Only users with the "Admin" role can access this view
    return HttpResponse("Welcome, Admin!")
