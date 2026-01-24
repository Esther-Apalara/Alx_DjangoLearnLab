from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


class UserProfile(models.Model):
    ROLE_ADMIN = "Admin"
    ROLE_LIBRARIAN = "Librarian"
    ROLE_MEMBER = "Member"

    ROLE_CHOICES = [
        (ROLE_ADMIN, "Admin"),
        (ROLE_LIBRARIAN, "Librarian"),
        (ROLE_MEMBER, "Member"),
    ]

    # ✅ Correct: points to the active user model (CustomUser)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

    def _str_(self):
        return f"{self.user.username} - {self.role}"


# ✅ Signal to auto-create profile for every new user
UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)