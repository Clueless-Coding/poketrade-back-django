from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name   = models.CharField(max_length=200)
    worth  = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()