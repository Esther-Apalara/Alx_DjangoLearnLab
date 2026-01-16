from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author, _ = Author.objects.get_or_create(name="Chinua Achebe")

book1, _ = Book.objects.get_or_create(title="Things Fall Apart", author=author)
book2, _ = Book.objects.get_or_create(title="No Longer at Ease", author=author)

library, _ = Library.objects.get_or_create(name="Central Library")
library.books.add(book1, book2)

librarian, _ = Librarian.objects.get_or_create(name="Grace", library=library)

# Queries

print("\n1) Books by Chinua Achebe:")
for book in Book.objects.filter(author__name="Chinua Achebe"):
    print("-", book.title)

print("\n2) Books in Central Library:")
for book in library.books.all():
    print("-", book.title)

print("\n3) Librarian for Central Library:")
print("-", library.librarian.name)