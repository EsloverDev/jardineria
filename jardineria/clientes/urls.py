from django.urls import path
from .views import inicioClientes

urlpatterns = [
    path('home/', inicioClientes, name='inicio')
]