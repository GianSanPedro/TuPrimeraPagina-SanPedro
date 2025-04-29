#ESTO ES CUENTAS VIEWS.PY
from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import VendorRequiredMixin, ClientRequiredMixin

from .forms import (
    EmailAuthenticationForm,
    ClienteRegistroForm,
    ClientePerfilForm,
    VendedorPerfilForm,
    UserEmailForm,
    OptionalPasswordChangeForm  
)

from concesionaria.models import Vehiculo, Venta


class LoginViewEmail(LoginView):
    template_name = 'cuentas/Login/login.html'
    authentication_form = EmailAuthenticationForm

    def get_success_url(self):
        if hasattr(self.request.user, 'perfil_cliente'):
            return reverse_lazy('cuentas:panel_cliente')
        return reverse_lazy('cuentas:panel_vendedor')

def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = ClienteRegistroForm()
    return render(request, 'cuentas/Registro/registro.html', {'form': form})


class PanelVendedorView(LoginRequiredMixin, VendorRequiredMixin, TemplateView):
    template_name = 'cuentas/PanelVendedor/panelVendedor.html'
    login_url     = reverse_lazy('cuentas:login')  # si no está logueado, va aquí

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        ctx['vehiculos_disponibles'] = user.vehiculos_cargados.filter(disponible=True)
        ctx['ventas_realizadas']     = user.ventas.select_related('vehiculo','cliente')
        return ctx

class PanelClienteView(LoginRequiredMixin, ClientRequiredMixin, TemplateView):
    template_name = 'cuentas/PanelCliente/panelCliente.html'
    login_url     = reverse_lazy('cuentas:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = self.request.user.perfil_cliente
        context['cliente'] = cliente
        context['compras'] = cliente.compras.select_related('vehiculo', 'vendedor')
        return context


@login_required
def perfil(request):
    return render(request, 'cuentas/Perfil/perfil.html', {'usuario': request.user})


@login_required
def editar_perfil(request):
    user = request.user
    is_cliente = hasattr(user, 'perfil_cliente')

    # perfil + avatar (Cliente) o perfil + avatar (Vendedor)
    if is_cliente:
        profile_form = ClientePerfilForm(
            request.POST or None,
            request.FILES or None,
            instance=user.perfil_cliente
        )
        email_form = UserEmailForm(
            request.POST or None,
            request.FILES or None,
            instance=user
        )
    else:
        profile_form = VendedorPerfilForm(
            request.POST or None,
            request.FILES or None,
            instance=user
        )
        email_form = None

    password_form = OptionalPasswordChangeForm(
        user,
        request.POST or None
    )

    if request.method == 'POST':
        perfil_ok = profile_form.is_valid()
        email_ok  = email_form.is_valid() if email_form else True

        old  = request.POST.get('old_password', '')
        new1 = request.POST.get('new_password1', '')
        new2 = request.POST.get('new_password2', '')
        cambio = any([old, new1, new2])
        password_ok = password_form.is_valid() if cambio else True

        if perfil_ok and email_ok and password_ok:
            profile_form.save()
            if email_form:
                email_form.save()
            if cambio:
                user = password_form.save()
                update_session_auth_hash(request, user)

            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('cuentas:perfil')

    return render(request, 'cuentas/Perfil/editar_perfil.html', {
        'profile_form':  profile_form,
        'email_form':    email_form,
        'password_form': password_form,
    })