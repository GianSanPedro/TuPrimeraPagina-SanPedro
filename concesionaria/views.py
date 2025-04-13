from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from .models import Vehiculo, Venta
from .forms import VehiculoForm
from .forms import EmailAuthenticationForm
from .forms import ClienteRegistroForm

def inicio(request):
    return render(request, 'concesionaria/Inicio/inicio.html')

def quienes(request):
    return render(request, 'concesionaria/QuienesSomos/quienes.html')

def login_view(request):
    return render(request, 'concesionaria/Login/login.html')

def vehiculos(request):
    tipo = request.GET.get('tipo', '')
    modelo = request.GET.get('modelo', '')
    año = request.GET.get('año', '')

    vehiculos_filtrados = Vehiculo.objects.all()

    if tipo:
        vehiculos_filtrados = vehiculos_filtrados.filter(tipo__icontains=tipo)
    if modelo:
        vehiculos_filtrados = vehiculos_filtrados.filter(modelo__icontains=modelo)
    if año:
        vehiculos_filtrados = vehiculos_filtrados.filter(año=año)

    return render(request, 'concesionaria/Vehiculos/vehiculos.html', {
        'vehiculos': vehiculos_filtrados
    })

@login_required
def crear_vehiculo(request):
    # Solo permitimos que lo usen vendedores (no clientes)
    if hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Solo los vendedores pueden cargar vehículos.")

    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.vendedor = request.user 
            vehiculo.save()
            return redirect('panel_vendedor')  
    else:
        form = VehiculoForm()
    
    return render(request, 'concesionaria/Vehiculos/crear_vehiculo.html', {'form': form})

@login_required
def editar_vehiculo(request, pk):
    if hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Acceso solo permitido para vendedores.")

    vehiculo = get_object_or_404(Vehiculo, pk=pk, vendedor=request.user)

    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('panel_vendedor')
    else:
        form = VehiculoForm(instance=vehiculo)

    return render(request, 'concesionaria/Vehiculos/editar_vehiculo.html', {'form': form})

@login_required
def eliminar_vehiculo(request, pk):
    if hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Acceso solo permitido para vendedores.")

    vehiculo = get_object_or_404(Vehiculo, pk=pk, vendedor=request.user)

    if request.method == 'POST':
        vehiculo.delete()
        return redirect('panel_vendedor')

    return render(request, 'concesionaria/Vehiculos/confirmar_eliminar.html', {'vehiculo': vehiculo})

@login_required
def comprar_vehiculo(request, pk):
    if not hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Solo los clientes pueden comprar vehículos.")

    vehiculo = get_object_or_404(Vehiculo, pk=pk, disponible=True)

    venta = Venta.objects.create(
        vehiculo=vehiculo,
        vendedor=vehiculo.vendedor,
        cliente=request.user.perfil_cliente,
        precio_final=vehiculo.precio,
        fecha=timezone.now()
    )
    vehiculo.disponible = False
    vehiculo.save()

    return redirect('panel_cliente')

class LoginViewEmail(LoginView):
    template_name = 'concesionaria/Login/login.html'
    authentication_form = EmailAuthenticationForm

    def get_success_url(self):
        if hasattr(self.request.user, 'perfil_cliente'):
            return reverse_lazy('panel_cliente')
        else:
            return reverse_lazy('panel_vendedor')

def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesion automáticamente
            return redirect('inicio')
    else:
        form = ClienteRegistroForm()
    return render(request, 'concesionaria/Registro/registro.html', {'form': form})

@login_required
def panel_vendedor(request):
    if hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Acceso solo permitido para vendedores.")

    # Vehiculos cargados por el vendedor que aun no se vendieron
    vehiculos_disponibles = request.user.vehiculos_cargados.filter(disponible=True)

    # Vehiculos vendidos 
    ventas_realizadas = request.user.ventas.select_related('vehiculo', 'cliente')

    return render(request, 'concesionaria/PanelVendedor/panelVendedor.html', {
        'vehiculos_disponibles': vehiculos_disponibles,
        'ventas_realizadas': ventas_realizadas
    })

@login_required
def panel_cliente(request):
    if not hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Solo los clientes pueden acceder a este panel.")

    cliente = request.user.perfil_cliente
    compras = cliente.compras.select_related('vehiculo', 'vendedor')

    return render(request, 'concesionaria/PanelCliente/panelCliente.html', {
        'cliente': cliente,
        'compras': compras,
    })