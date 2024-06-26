from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(default='default@example.com')  # Add a default value here

class Contact(models.Model):
    owner = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

class SpamNumber(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    reports = models.PositiveIntegerField(default=0)
