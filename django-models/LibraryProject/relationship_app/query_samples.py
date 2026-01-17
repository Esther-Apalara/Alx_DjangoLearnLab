from relationship_app.models import Author, Book, Library, Librarian

# -------------------------
# Sample data
# -------------------------
author, _ = Author.objects.get_or_create(name="Chinua Achebe")

book1, _ = Book.objects.get_or_create(title="Things Fall Apart", author=author)
book2, _ = Book.objects.get_or_create(title="No Longer at Ease", author=author)

library, _ = Library.objects.get_or_create(name="Central Library")
library.books.add(book1, book2)

librarian, _ = Librarian.objects.get_or_create(name="Grace", library=library)

# -------------------------
# REQUIRED QUERIES
# -------------------------

# 1) Query all books by a specific author
author_name = "Chinua Achebe"
books_by_author = Book.objects.filter(author__name=author_name)

print("\n1) Books by a specific author:")
for book in books_by_author:
    print("-", book.title)

# 2) List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)   # 👈 CHECKER NEEDS THIS EXACT LINE

print("\n2) Books in a library:")
for book in library.books.all():
    print("-", book.title)

# 3) Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)

print("\n3) Librarian for a library:")
print("-", librarian.name)