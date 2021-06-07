from django.db import models
from .mechanic import Mechanic
from .person import Person

class Request(models.Model):
    description = models.CharField(max_length=150, null=False, blank=False)
    latitude = models.CharField(max_length=20, null=False, blank=False)
    longitude = models.CharField(max_length=20, null=False, blank=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    created_ts = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description