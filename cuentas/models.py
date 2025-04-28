from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Vendedor(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  

    telefono = models.CharField(max_length=20, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.email}"


class Cliente(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_cliente'
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"