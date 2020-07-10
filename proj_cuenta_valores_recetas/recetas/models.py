from django.db import models

# Create your models here.
class Ingredientes(models.Model):
    nombre_ingrediente= models.CharField(verbose_name='Ingrediente', max_length=70, null=True, blank=True)
    cantidad= models.DecimalField(verbose_name='Cantidad', max_digits=6, decimal_places=2)

    class Meta:
        verbose_name= 'Ingrediente'
        verbose_name_plural= 'Ingredientes'

class Recetas(models.Model):
    titulo= models.CharField(verbose_name='Titulo', max_length=80)
    ingredientes= models.ManyToManyField(Ingredientes, null=True, blank= True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name= 'Receta'
        verbose_name_plural= 'Recetas'