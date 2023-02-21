from django.db import models
from django.utils import timezone

class Drink(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name