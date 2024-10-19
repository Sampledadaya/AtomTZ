from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_moderator = models.BooleanField(default=False)  # Добавление поля is_moderator
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='atom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='atom_user_permissions',
        blank=True,
    )
