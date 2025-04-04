from django.db import models

class CategoriaCliente(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    envio_gratis = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateField()
    categoria = models.ForeignKey(CategoriaCliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre if self.categoria else 'Sin categoría'})"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado')
    ], default='pendiente')

    def __str__(self):
        return f"Pedido {self.id} - {self.estado}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"


