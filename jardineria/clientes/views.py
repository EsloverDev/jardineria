from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
def inicioClientes(request):
    return HttpResponse("<h1>Hola mundo desde Clientes!</h1>")

def goIndex(request):
    data = {'usuario': 'Diana'}
    return render(request, 'index.html', data)

def parametrosURL(request, cliente_id):
    data = Cliente.objects.get(id=cliente_id)
    return render(request, 'cliente.html', {'cliente': data})
