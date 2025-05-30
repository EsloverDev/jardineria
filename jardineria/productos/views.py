from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto, Categoria, Proveedor
from django.contrib import messages

def indexProductos(request):
    categorias = Categoria.objects.all()
    productos_por_categoria = {}

    for categoria in categorias:
        productos = Producto.objects.filter(categoria=categoria)
        productos_por_categoria[categoria.nombre] = productos
    return render(request, 'productos/index.html', {
        'productos_por_categoria': productos_por_categoria
    })

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripción')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')
        proveedor_id = request.POST.get('proveedor')
        imagen = request.FILES.get('imagen')

        categoria = Categoria.objects.get(pk=categoria_id) if categoria_id else None
        proveedor = Proveedor.objects.get(pk=proveedor_id) if proveedor_id else None

        Nuevo_producto = Producto(
            nombre = nombre,
            descripcion = descripcion,
            precio = precio,
            stock = stock,
            categoria = categoria,
            proveedor = proveedor,
            imagen = imagen
        )
        Nuevo_producto.save()
        messages.success(request, 'Producto creado correctamente')
        return redirect('productos:index')
    
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'productos/formulario_producto.html', {
        'categorias': categorias,
        'proveedores': proveedores,
        'accion': 'Crear'
    })