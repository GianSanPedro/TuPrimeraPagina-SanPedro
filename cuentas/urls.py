from django.urls import path
from . import views
from .views import (LoginViewEmail, registro_cliente, PanelVendedorView, PanelClienteView, perfil, editar_perfil,)
from django.contrib.auth.views import LogoutView

app_name = 'cuentas'

urlpatterns = [
    path('Login/',     LoginViewEmail.as_view(),    name='login'),
    path('Logout/',    LogoutView.as_view(),        name='logout'),
    path('Registro/',  registro_cliente,            name='registro'),
    path('PanelVendedor/', PanelVendedorView.as_view(), name='panel_vendedor'),
    path('PanelCliente/', PanelClienteView.as_view(), name='panel_cliente'),
    path('Perfil/',    perfil,                      name='perfil'),
    path('Perfil/editar/', editar_perfil,           name='editar_perfil'),
]