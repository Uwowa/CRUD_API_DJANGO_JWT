from django.db import models

# Create your models here.
class Programmer(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    edad = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
