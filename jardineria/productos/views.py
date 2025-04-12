from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

def inicioProductos(request):
    return HttpResponse("<h1>Hola mundo desde Productos!</h1>")

def parametrosUrl(request,producto_id):
    data = Producto.objects.get(id=producto_id)
    return render(request,'producto.html',{'producto': data})
