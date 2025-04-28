from django.contrib import admin
from .models import Vendedor, Cliente

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'telefono', 'fecha_ingreso', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellido', 'dni', 'telefono')
    search_fields = ('nombre', 'apellido', 'dni', 'usuario__email')