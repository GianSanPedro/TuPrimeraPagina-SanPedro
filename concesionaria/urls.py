from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('vehiculos/nuevo/', views.crear_vehiculo, name='crear_vehiculo'),
    path('quienes/', views.quienes, name='quienes'),
    path('login/', views.login_view, name='login'),
]
