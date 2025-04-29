# concesionaria/models.py

from django.conf import settings
from django.db import models
from cuentas.models import Cliente, Vendedor


class Vehiculo(models.Model):
    TIPO_CHOICES = [
        ('auto', 'Auto'),
        ('camioneta', 'Camioneta'),
        ('moto', 'Moto'),
    ]

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vehiculos_cargados'
    )
    foto = models.ImageField(
        upload_to='vehiculos/',
        null=False,
        blank=False,
        help_text="Sube aquí la foto del vehículo"
    )

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='ventas')
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='compras')
    fecha = models.DateField(auto_now_add=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cliente} compró {self.vehiculo} a {self.vendedor} en {self.fecha}"
