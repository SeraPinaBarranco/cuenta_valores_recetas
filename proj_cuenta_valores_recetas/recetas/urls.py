from django.urls import include, path
from .views import *

urlpatterns = [
    path('', RecetasIndex.as_view(), name='indice_recetas' ),  
    path('crear_recetas', RecetasCreate.as_view(), name='crear_recetas' ),    
]