from django.urls import path
from .views import indexProductos, crear_producto

app_name = 'productos'

urlpatterns = [
    path('', indexProductos, name='index'),
    path('crear/', crear_producto, name='crear'),
    #path('editar/<int:id>', editar_producto, name='editar'),
    #path('eliminar/<int:id>', eliminar_producto, name='eliminar')
]