from django.db import models

# Create your models here.
class Receta(models.Model):
    titulo= models.CharField(verbose_name='Titulo')
    