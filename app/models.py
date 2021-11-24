from django.db import models

# Create your models here.

class Datos(models.Model):
    dato = models.CharField(max_length=50)
    valor = models.IntegerField()