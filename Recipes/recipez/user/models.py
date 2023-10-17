from django.db import models
from django.contrib.auth.models import AbstractUser

from recipe.models import Ingredient

class User(AbstractUser):
    # Add custom user fields if needed
    nickname = models.CharField(max_length=100, null=True)
    shopping_list = models.ManyToManyField(Ingredient)


    