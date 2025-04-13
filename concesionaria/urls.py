from django.urls import path
from . import views
from .views import LoginViewEmail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('vehiculos/nuevo/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculo/editar/<int:pk>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculo/eliminar/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('quienes/', views.quienes, name='quienes'),
    path('login/', LoginViewEmail.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_cliente, name='registro'),
    path('panel-vendedor/', views.panel_vendedor, name='panel_vendedor'),
    path('panel-cliente/', views.panel_cliente, name='panel_cliente'),
    path('vehiculo/comprar/<int:pk>/', views.comprar_vehiculo, name='comprar_vehiculo'),
]
