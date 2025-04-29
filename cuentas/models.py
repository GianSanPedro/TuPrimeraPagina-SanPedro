from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Vendedor(AbstractUser):
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)

    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        help_text="Sube aquí tu foto de perfil"
    )
    fecha_nacimiento = models.DateField(null=True,blank=True,help_text="Fecha de nacimiento")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email}"
    
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


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
    fecha_nacimiento = models.DateField(null=True,blank=True,help_text="Fecha de nacimiento")

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"