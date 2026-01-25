from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.db.models import Q

from .models import Book
from .forms import BookSearchForm


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    return HttpResponse("✅ You can VIEW books.")


@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    return HttpResponse("✅ You can CREATE books.")


@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    return HttpResponse(f"✅ You can EDIT book with id={pk}.")


@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    return HttpResponse(f"✅ You can DELETE book with id={pk}.")


def csrf_example(request):
    return render(request, "bookshelf/form_example.html")


@permission_required("bookshelf.can_view", raise_exception=True)
def safe_search(request):
    """
    Secure search view:
    - Uses a Django Form to validate/sanitize input
    - Uses Django ORM (parameterized) to prevent SQL injection
    """
    form = BookSearchForm(request.GET)
    books = Book.objects.none()

    if form.is_valid():
        q = form.cleaned_data.get("q", "")
        if q:
            books = Book.objects.filter(Q(title_icontains=q) | Q(author_icontains=q))
        else:
            books = Book.objects.all()

    # Return simple text response (no template required)
    results = ", ".join([b.title for b in books]) if books.exists() else "No results"
    return HttpResponse(f"Search results: {results}")