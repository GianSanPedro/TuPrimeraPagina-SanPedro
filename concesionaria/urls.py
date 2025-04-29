from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('vehiculos/nuevo/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculo/editar/<int:pk>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculo/eliminar/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('quienes/', views.quienes, name='quienes'),
    path('acerca/', views.about, name='acerca'),
    path('vehiculo/comprar/<int:pk>/', views.comprar_vehiculo, name='comprar_vehiculo'),
]
