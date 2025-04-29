#ESTO ES CONCESIONARIA VIEWS.PY
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone

from .models import Vehiculo, Venta
from .forms import VehiculoForm


def inicio(request):
    return render(request, 'concesionaria/Inicio/inicio.html')


def quienes(request):
    return render(request, 'concesionaria/QuienesSomos/quienes.html')


def vehiculos(request):
    tipo   = request.GET.get('tipo', '')
    modelo = request.GET.get('modelo', '')
    año    = request.GET.get('año', '')

    qs = Vehiculo.objects.all()
    if tipo:
        qs = qs.filter(tipo__icontains=tipo)
    if modelo:
        qs = qs.filter(modelo__icontains=modelo)
    if año:
        qs = qs.filter(año=año)

    return render(request, 'concesionaria/Vehiculos/vehiculos.html', {
        'vehiculos': qs
    })


def about(request):
    return render(request, 'concesionaria/Acerca de mi/About.html')


@login_required
def crear_vehiculo(request):
    # Solo vendedores (no clientes) pueden crear vehículos
    if hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Solo los vendedores pueden cargar vehículos.")

    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.vendedor = request.user
            vehiculo.save()
            return redirect('cuentas:panel_vendedor')
    else:
        form = VehiculoForm()

    return render(request,'concesionaria/Vehiculos/crear_vehiculo.html',{'form': form})


@login_required
def editar_vehiculo(request, pk):
    # Solo vendedores pueden editar sus propios vehículos
    if hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Acceso solo permitido para vendedores.")

    vehiculo = get_object_or_404(Vehiculo, pk=pk, vendedor=request.user)

    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('cuentas:panel_vendedor')
    else:
        form = VehiculoForm(instance=vehiculo)

    return render(request,'concesionaria/Vehiculos/editar_vehiculo.html',{'form': form, 'vehiculo': vehiculo})


@login_required
def eliminar_vehiculo(request, pk):
    # Solo vendedores pueden eliminar sus propios vehículos
    if hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Acceso solo permitido para vendedores.")

    vehiculo = get_object_or_404(Vehiculo, pk=pk, vendedor=request.user)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('cuentas:panel_vendedor')

    return render(request,'concesionaria/Vehiculos/confirmar_eliminar.html',{'vehiculo': vehiculo})


@login_required
def comprar_vehiculo(request, pk):
    # Solo clientes pueden comprar vehículos
    if not hasattr(request.user, 'perfil_cliente'):
        return HttpResponseForbidden("Solo los clientes pueden comprar vehículos.")

    vehiculo = get_object_or_404(Vehiculo, pk=pk, disponible=True)
    Venta.objects.create(
        vehiculo     = vehiculo,
        vendedor     = vehiculo.vendedor,
        cliente      = request.user.perfil_cliente,
        precio_final = vehiculo.precio,
        fecha        = timezone.now()
    )
    vehiculo.disponible = False
    vehiculo.save()
    return redirect('cuentas:panel_cliente')
