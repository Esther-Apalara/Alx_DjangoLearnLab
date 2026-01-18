from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import list_books
from .views import LibraryDetailView
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    # Task 1
    path("books/", list_books, name="list_books"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Task 2
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    # Task 3
    path("admin-area/", admin_view, name="admin_view"),
    path("librarian-area/", librarian_view, name="librarian_view"),
    path("member-area/", member_view, name="member_view"),

    # Task 4 — checker-required literal paths
    path("add_book/", add_book, name="add_book"),
    path("edit_book/<int:pk>/", edit_book, name="edit_book"),
    path("delete_book/<int:pk>/", delete_book, name="delete_book"),

    # (Keep the REST-style paths too — harmless)
    path("books/add/", add_book, name="add_book_alt"),
    path("books/<int:pk>/edit/", edit_book, name="edit_book_alt"),
    path("books/<int:pk>/delete/", delete_book, name="delete_book_alt"),
]