from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    created_ts = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.email
