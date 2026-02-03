from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer handles serialization of Book model data
# and includes custom validation logic.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


        # AuthorSerializer serializes Author data
# and includes nested serialization of related books.
class AuthorSerializer(serializers.ModelSerializer):
    # 'books' comes from related_name='books' in the Book model
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']