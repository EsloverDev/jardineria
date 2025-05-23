from django.urls import path
from .views import indexProductos, parametrosUrl

app_name = 'productos'

urlpatterns = [
    path('', indexProductos, name='index'),
    path('producto/<int:producto_id>',parametrosUrl, name='producto')
]