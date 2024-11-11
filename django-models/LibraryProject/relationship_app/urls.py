from django.urls import path
from . import views
from .views import list_books, CustomLoginView, CustomLogoutView, register

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]

urlpatterns = [
    path('login/', CustomLoginView.as_view(), template_name='login'),
    path('logout/', CustomLogoutView.as_view(), template_name='logout'),
    path('register/', register, name='register'),
    # Add other URLs for your app here
]