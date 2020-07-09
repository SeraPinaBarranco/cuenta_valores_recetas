from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Recetas
from .forms import FormRecetas

# Create your views here.
class RecetasIndex(TemplateView):
    template_name = "recetas/indice_recetas.html"

    
    def get_context_data(self, **kwargs):
        context = super(RecetasIndex, self).get_context_data(**kwargs)
        context['titulo'] = 'Indice recetas'
        return context
    
class RecetasCreate(CreateView):
    model= Recetas
    #fields= '__all__'
    form_class = FormRecetas
    #template_name = "recetas/crear_recetas.html"
    success_url = reverse_lazy('recetas:indice_recetas')