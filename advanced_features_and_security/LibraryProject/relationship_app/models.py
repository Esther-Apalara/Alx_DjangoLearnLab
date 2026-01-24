from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    class Meta:
        permissions = (
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        )

    def _str_(self):
        return f"{self.title} by {self.author.name}"


class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="libraries")

    def _str_(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def _str_(self):
        return f"{self.name} (Librarian of {self.library.name})"


class UserProfile(models.Model):
    ROLE_ADMIN = "Admin"
    ROLE_LIBRARIAN = "Librarian"
    ROLE_MEMBER = "Member"

    ROLE_CHOICES = [
        (ROLE_ADMIN, "Admin"),
        (ROLE_LIBRARIAN, "Librarian"),
        (ROLE_MEMBER, "Member"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

    def _str_(self):
        return f"{self.user.username} - {self.role}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)