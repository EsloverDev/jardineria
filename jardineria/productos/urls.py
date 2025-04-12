from django.urls import path
from .views import inicioProductos, parametrosUrl

urlpatterns = [
    path('home/', inicioProductos, name='inicio'),
    path('producto/<int:producto_id>',parametrosUrl, name='producto')
]