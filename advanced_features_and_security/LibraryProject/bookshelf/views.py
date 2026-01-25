from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required


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