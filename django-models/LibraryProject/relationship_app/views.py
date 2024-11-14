from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from django.http import HttpResponse
from .models import Author, Book, Librarian, Library

from django.contrib.auth.models import User

# Create your views here.

def booklist(request):
    books = Book.objects.all()
    context = {'books':books}

    return render(request, 'relationship_app/list_books.html',context=context)

class LibraryListView(DetailView):
    model = Library
    template_name = 'relationship_app/librarylist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context


from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import UserProfile

def has_role(user, role):
    return UserProfile.objects.filter(user=user.id, role=role).exists()
def is_admin(user):
    return has_role(user, "Admin")
def is_librarian(user):
    return has_role(user, "Librarian")
def is_member(user):
    return has_role(user, "Member")

# Views for Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# View for Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# View for Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class register(CreateView): 
    form_class = UserCreationForm()
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class ProfileView(TemplateView):
    template_name = 'relationship_app/profile.html'
    # user = self.get_object
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # user = self.get_object()
        context["user"] = self.request.user
        return context
    
from django.contrib.auth.views import LoginView, LogoutView

class login(LoginView):
    template_name = 'relationship_app/login.html'

class logout(LogoutView):
    template_name = 'relationship_app/logout.html'