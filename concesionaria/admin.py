from django.contrib import admin
from .models import Vehiculo, Venta



@admin.action(description="Marcar vehículos como no disponibles")
def marcar_como_no_disponibles(modeladmin, request, queryset):
    queryset.update(disponible=False)

@admin.action(description="Marcar vehículos como disponibles")
def marcar_como_disponibles(modeladmin, request, queryset):
    queryset.update(disponible=True)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'tipo', 'año', 'precio', 'disponible', 'vendedor')
    search_fields = ('marca', 'modelo', 'tipo')
    list_filter = ('tipo', 'disponible', 'año')
    actions = [marcar_como_no_disponibles, marcar_como_disponibles]


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'vendedor', 'cliente', 'fecha', 'precio_final')
    search_fields = ('vehiculo__marca', 'vehiculo__modelo', 'cliente__apellido', 'vendedor__email')
    list_filter = ('fecha',)

