from django.shortcuts import render
from django.http import HttpResponse

def inicioClientes(request):
    return HttpResponse("<h1>Hola mundo desde Clientes!</h1>")

