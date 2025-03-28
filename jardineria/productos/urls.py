from django.urls import path
from .views import inicioProductos

urlpatterns = [
    path('home/', inicioProductos, name='inicio')
]