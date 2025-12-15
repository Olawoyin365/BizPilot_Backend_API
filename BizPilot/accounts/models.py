from django.contrib.auth.models import AbstractUser
from django.db import models
from categories.models import Category
from django_countries.fields import CountryField

"""
    Custom user model that extends Django's AbstractUser.
    AbstractUser already provides:
    -username, -first_name, -last_name, -email, -password, -permissions fields
    And, references category as FK using modular approach
"""

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    #username = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    country = CountryField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

""" email is set to be required for login which overrides the Django default username 
Also, stated built in fields would be populated for signup """

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

def __str__(self):
        return self.username
