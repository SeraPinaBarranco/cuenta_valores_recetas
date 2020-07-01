from django.urls import include, path
from .views import RecetasIndex

urlpatterns = [
    path('', RecetasIndex.as_view(), name='indice_recetas' ),    
]