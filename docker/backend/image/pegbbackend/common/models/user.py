from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    username = None
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
