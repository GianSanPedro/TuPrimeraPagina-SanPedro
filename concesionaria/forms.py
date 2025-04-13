from django import forms
from .models import Vehiculo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Vendedor, Cliente

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'tipo', 'año', 'precio', 'disponible']

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

class ClienteRegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.CharField(max_length=20)
    telefono = forms.CharField(max_length=20)

    class Meta:
        model = Vendedor  # porque es el AUTH_USER_MODEL
        fields = ['email', 'password1', 'password2', 'nombre', 'apellido', 'dni', 'telefono']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email'] 
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Cliente.objects.create(
                usuario=user,
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                dni=self.cleaned_data['dni'],
                telefono=self.cleaned_data['telefono']
            )
        return user