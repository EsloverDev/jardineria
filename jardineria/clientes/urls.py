from django.urls import path
from .views import login, indexClientes, parametrosURL

app_name = 'clientes'

urlpatterns = [
    path('', indexClientes, name='index'),
    path('login/', login, name='login'),
    path('cliente/<int:cliente_id>/', parametrosURL, name='cliente')
]