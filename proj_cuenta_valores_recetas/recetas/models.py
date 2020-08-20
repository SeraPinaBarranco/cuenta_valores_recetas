from django.forms import model_to_dict
from django.db import models

# Create your models here.
class Productos(models.Model):
    producto= models.CharField(verbose_name='Producto', max_length=70, null=True, blank=True)
    calorias = models.DecimalField(verbose_name='Calorias', max_digits=6, decimal_places=2)
    grasas= models.DecimalField(verbose_name='Grasas', max_digits=6, decimal_places=2)

    def __str__(self):
        return self.producto

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural= 'Productos'

class Ingredientes(models.Model):
    nombre_ingrediente= models.ForeignKey(Productos, on_delete=models.CASCADE, null= True, blank= True)
    cantidad= models.DecimalField(verbose_name='Cantidad', max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.nombre_ingrediente )

    class Meta:
        verbose_name= 'Ingrediente'
        verbose_name_plural= 'Ingredientes'

class Recetas(models.Model):
    titulo= models.CharField(verbose_name='Titulo', max_length=80)
    ingredientes= models.ManyToManyField(Ingredientes, null=True, blank= True, related_name='ingredientes')

    def __str__(self):
        return self.titulo 

    class Meta:
        verbose_name= 'Receta'
        verbose_name_plural= 'Recetas'

