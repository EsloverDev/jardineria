from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

def indexProductos(request):
    return render(request, 'productos/index.html')

def parametrosUrl(request,producto_id):
    data = Producto.objects.get(id=producto_id)
    return render(request,'producto.html',{'producto': data})
