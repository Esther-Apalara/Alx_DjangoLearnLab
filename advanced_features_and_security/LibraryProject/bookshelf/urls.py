from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("create/", views.book_create, name="book_create"),
    path("edit/<int:pk>/", views.book_edit, name="book_edit"),
    path("delete/<int:pk>/", views.book_delete, name="book_delete"),
    path("csrf-example/", views.csrf_example, name="csrf_example"),
    path("safe-search/", views.safe_search, name="safe_search"),
]