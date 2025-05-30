from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, CategoriaCliente, Pedido
from django.utils import timezone

def index(request):
    return render(request, 'index.html')

def indexClientes(request):
    return render(request, 'clientes/index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        clave = request.POST.get('password')
        try:
            cliente = Cliente.objects.get(email=email, clave=clave)
            return redirect('clientes:perfil', cliente_id=cliente.id)
        except Cliente.DoesNotExist:
            return render(request, 'clientes/index.html', {'error': 'Correo o contraseña incorrectos'})
    return render(request, 'clientes/index.html')

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('email')
        telefono = request.POST.get('telefono')
        clave = request.POST.get('clave')

        try:
            categoria = CategoriaCliente.objects.get(nombre = 'General')
            cliente = Cliente.objects.create(
                nombre = nombre,
                apellido = apellido,
                email = correo,
                telefono = telefono,
                fecha_registro = timezone.now().date(),
                clave = clave,
                categoria = categoria
            )
            return redirect('clientes:login')
        except:
            error = "ya existe un cliente con ese correo"
            return render(request, 'clientes/registro.html', {'error': error})
    return render(request, 'clientes/registro.html')

def perfil(request, cliente_id):
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        pedidos = Pedido.objects.filter(cliente=cliente).order_by('-fecha_pedido')
        return render(request, 'clientes/perfil.html', {
            'cliente': cliente,
            'pedidos': pedidos,
            })
    except Cliente.DoesNotExist:
        return HttpResponse("Cliente no encontrado", status=404)