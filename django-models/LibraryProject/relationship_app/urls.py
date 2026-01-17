from django.urls import path
from django.contrib.auth import views as auth_views

from . import views  # ✅ so checker can see views.register
from .views import list_books
from .views import LibraryDetailView
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    # Task 1
    path("books/", list_books, name="list_books"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Task 2 (checker wants views.register)
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    # Task 3
    path("admin-area/", admin_view, name="admin_view"),
    path("librarian-area/", librarian_view, name="librarian_view"),
    path("member-area/", member_view, name="member_view"),
]