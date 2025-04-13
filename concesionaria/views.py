from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import VehiculoForm

def inicio(request):
    return render(request, 'concesionaria/Inicio/inicio.html')

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
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculos')
    else:
        form = VehiculoForm()
    
    return render(request, 'concesionaria/Vehiculos/crear_vehiculo.html', {'form': form})

def quienes(request):
    return render(request, 'concesionaria/QuienesSomos/quienes.html')

def login_view(request):
    return render(request, 'concesionaria/Login/login.html')
