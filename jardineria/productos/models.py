from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.CharField(max_length=50, choices=[
        ('fertilizantes', 'Fertilizantes'),
        ('herramientas', 'Herramientas'),
        ('plantas', 'Plantas'),
        ('materas', 'Materas'),
        ('otros', 'Otros'),
    ])
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
