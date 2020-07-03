from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RecetasIndex(TemplateView):
    template_name = "recetas/indice_recetas.html"

    
    def get_context_data(self, **kwargs):
        context = super(RecetasIndex, self).get_context_data(**kwargs)
        context['titulo'] = 'Indice recetas'
        return context
    
class RecetasCreate(TemplateView):
    template_name = "recetas/crear_recetas.html"