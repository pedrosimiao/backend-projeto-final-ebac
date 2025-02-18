from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_custom_groups",  # Evita conflito com auth.User
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_custom_permissions",  # Evita conflito com auth.User
        blank=True
    )

    def __str__(self):
        return self.username