from django.shortcuts import render
from django.http import HttpResponse

def inicioProductos(request):
    return HttpResponse("<h1>Hola mundo desde Productos!</h1>")
