from django.contrib import admin
from .models import CategoriaCliente, Cliente, Pedido, DetallePedido

admin.site.register(Cliente)
admin.site.register(CategoriaCliente)
admin.site.register(Pedido)
admin.site.register(DetallePedido)