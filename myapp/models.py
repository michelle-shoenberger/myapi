from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class Drink(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    description = models.TextField()
    bread = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class User(AbstractUser):
    # inherits from all user fields
    # AbstractBaseUser - only has password hashing
    first = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True) # optional in base user
    is_premium = models.BooleanField(default=False)
    #profile_pic = models.ImageField(blank=True) - need Pillow

    USERNAME_FIELD = 'email' # username by default
    REQUIRED_FIELDS = []   #username and password are required by default (now email)

    def __str__(self):
        return self.username

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)