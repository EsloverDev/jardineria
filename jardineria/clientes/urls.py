from django.urls import path
from .views import inicioClientes, goIndex, parametrosURL


urlpatterns = [
    path('home/', inicioClientes, name='inicio'),
    path('index', goIndex, name='index'),
    path('cliente/<int:cliente_id>/', parametrosURL, name='cliente')
]