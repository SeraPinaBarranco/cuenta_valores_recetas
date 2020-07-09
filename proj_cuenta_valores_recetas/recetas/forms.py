from django import forms

from .models import Recetas

class FormRecetas(forms.Form):
    nombre_receta= forms.CharField(label='Título', max_length=80)