from django.urls import path
from . import views
from .views import LoginViewEmail, registro_cliente, panel_vendedor, panel_cliente, editar_perfil
from django.contrib.auth.views import LogoutView

app_name = 'cuentas'

urlpatterns = [
    path('Login/', LoginViewEmail.as_view(),    name='login'),
    path('Logout/', LogoutView.as_view(),       name='logout'),
    path('Registro/', registro_cliente,         name='registro'),
    path('PanelVendedor/', panel_vendedor,      name='panel_vendedor'),
    path('PanelCliente/', panel_cliente,        name='panel_cliente'),
    path('Perfil/', views.perfil,               name='perfil'),
    path('Perfil/editar/', views.editar_perfil, name='editar_perfil'),
]
