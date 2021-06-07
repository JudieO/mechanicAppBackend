from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Mechanic(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    latitude = models.CharField(max_length=50, null=False, blank=False)
    longitude = models.CharField(max_length=50, null=False, blank=False)
    requested = models.BooleanField(default=False, null=False, blank=False)
    total_orders = models.IntegerField(null=False, default=0)
    created_ts = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
