from django.urls import path
from . import views

urlpatterns = [
    path('booklist/',views.booklist, name = "booklist"),
    path('librarylist/<int:pk>/',views.LibraryListView.as_view(), name ="librarylist"),
    path('adminsonly/', views.AdminOnlyView, name = "adminsonly"),
    path('librarian/', views.LibrarianView, name = "librarian"),
    path('login/', views.login.as_view(), name = 'login'),
    path('logout/',views.logout.as_view(), name = 'logout'),
    path('register/',views.register.as_view(), name = 'register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]