from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Pokemon(models.Model):
    name   = models.CharField(max_length=200)
    worth  = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    image  = models.URLField()
    types  = models.JSONField()


class User(AbstractUser):
    pokemons = models.ManyToManyField(Pokemon)

