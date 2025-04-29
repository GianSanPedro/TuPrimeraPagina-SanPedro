from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Vendedor, Cliente

@admin.register(Vendedor)
class VendedorAdmin(UserAdmin):
    model = Vendedor

    # Campos que se verán en la lista
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter  = ('is_staff', 'is_active')

    # Organización de campos en el detalle
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Info personal', {
            'fields': (
                'first_name', 'last_name',
                'telefono', 'fecha_ingreso',
                'fecha_nacimiento', 'avatar'
            )
        }),
        ('Permisos', {
            'fields': (
                'is_staff', 'is_active',
                'is_superuser', 'groups', 'user_permissions'
            )
        }),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos al crear un nuevo superusuario/vendedor
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    search_fields = ('email',)
    ordering     = ('email',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    list_display = ('usuario', 'nombre', 'apellido', 'dni', 'telefono', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido', 'dni')
