from django.urls import path
from . import views

urlpatterns = [
    path('booklist/',views.booklist, name = "booklist"),
    path('librarylist/<int:pk>/',views.LibraryListView.as_view(), name ="librarylist"),
    path('adminsonly/', views.admin_view, name = "admin"),
    path('librarian/', views.librarian_view, name = "librarian"),
    path('member/', views.member_view, name = 'member'),
    path('login/', views.login.as_view(), name = 'login'),
    path('logout/',views.logout.as_view(), name = 'logout'),
    path('register/',views.register.as_view(), name = 'register'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('admin/', views.admin_view, name = 'admin_view'),
    path('librarian/', views.librarian_view, name = 'librarian_view'),
    path('member/', views.member_view, name = 'member_view'),
    path('add_book/', views.add_book, name = 'add_book'),
    path('edit_book/', views.edit_book, name = 'edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
]