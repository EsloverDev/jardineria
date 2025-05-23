from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def indexClientes(request):
    return render(request, 'clientes/index.html')

def login(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'clientes/index.html', {'error': 'Credenciales incorrectas'})
    else:
        return redirect('clientes:index')

"""def indexClientes(request):
    data = {'usuario': 'Diana'}
    return render(request, '../templates/index.html', data)
"""

def parametrosURL(request, cliente_id):
    data = Cliente.objects.get(id=cliente_id)
    return render(request, 'cliente.html', {'cliente': data})
