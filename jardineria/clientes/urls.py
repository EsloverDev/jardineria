from django.urls import path
from .views import login, indexClientes, registro, perfil

app_name = 'clientes'

urlpatterns = [
    path('', indexClientes, name='index'), 
    path('login/', login, name='login'),
    path('perfil/<int:cliente_id>/', perfil, name='perfil'),
    path('registro/', registro, name='registro')
]