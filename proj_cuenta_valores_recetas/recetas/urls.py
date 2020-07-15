from django.urls import include, path
from .views import RecetasCreate, RecetasIndex, RecetasListView, RecetasDelete, ProductosListView, ProductosCreate

urlpatterns = [
    path('', RecetasIndex.as_view(), name='indice_recetas' ),  
    path('crear_recetas', RecetasCreate.as_view(), name='crear_recetas' ),    
    path('listar_recetas', RecetasListView.as_view(), name='listar_recetas' ),
    path('eliminar_receta/<pk>', RecetasDelete.as_view(), name='eliminar_receta' ),
    path('listar_productos', ProductosListView.as_view(), name='listar_productos' ),
    path('crear_producto', ProductosCreate.as_view(), name='crear_producto' ),

]