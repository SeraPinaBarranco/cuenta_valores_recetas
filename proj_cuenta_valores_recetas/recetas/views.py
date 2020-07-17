from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Productos, Recetas, Ingredientes
from .forms import FormRecetas, FormProductos

# Create your views here.
###VISTAS DE RECETAS#####
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
    success_url = reverse_lazy('listar_recetas')

    
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

class RecetasDelete(DeleteView):
    #form_class= FormRecetas
    model = Recetas
    success_url = reverse_lazy('listar_recetas')

class RecetasUpdate(UpdateView):
    model = Recetas  
    form_class = FormRecetas  
    #fields = ['titulo']
    success_url = reverse_lazy('listar_recetas')
##########################

###VISTAS DE PRODUCTOS####
class ProductosListView(ListView):
    model = Productos
    #paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']= 'Listado de productos'
        return context

class ProductosCreate(CreateView):
    #model= Recetas
   
    form_class = FormProductos
    template_name = "recetas/crear_productos.html"
    success_url = reverse_lazy('listar_productos')

    
    def get_context_data(self, **kwargs):
        context = super(ProductosCreate, self).get_context_data(**kwargs)
        context['titulo']= 'Crear Producto'
        return context
##########################

###VISTAS DE INGREDIENTES####
class IngredientesCreate(CreateView):
    model= Ingredientes     
    success_url = reverse_lazy('listar_recetas')
    fields= '__all__'

    
    def get_context_data(self, **kwargs):
        context = super(IngredientesCreate, self).get_context_data(**kwargs)
        context['productos'] = Productos.objects.all()
        context['titulo']= 'Añadir Ingrediente'
        return context

    
