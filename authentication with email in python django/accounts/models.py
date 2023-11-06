from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class CustomUser(AbstractUser):
#     email = models.EmailField(max_length=100, unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
