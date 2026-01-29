from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def home(request):
    return HttpResponse("Welcome to the API!")    