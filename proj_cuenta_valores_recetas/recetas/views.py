from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
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
    #model= Recetas
   
    form_class = FormRecetas
    template_name = "recetas/crear_recetas.html"
    success_url = reverse_lazy('indice_recetas')

    
    def get_context_data(self, **kwargs):
        context = super(RecetasCreate, self).get_context_data(**kwargs)
        context['titulo']= 'Crear Receta'
        return context
    
class RecetasListView(ListView):

    model = Recetas

    #paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']= 'Listado de recetas'
        return context
    