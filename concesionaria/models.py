# concesionaria/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Vendedor(AbstractUser):
    # El campo username, email y password ya existen por herencia
    # Podés agregar más si querés:
    telefono = models.CharField(max_length=20, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.email})"


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"



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
