from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import Vendedor, Cliente

User = get_user_model()


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )


class ClienteRegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    nombre = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    apellido = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    dni = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telefono = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    avatar = forms.ImageField(required=False)
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type':'date','class':'form-control'})
    )

    class Meta:
        model  = Vendedor
        fields = [
            'email', 'password1', 'password2',
            'nombre', 'apellido', 'dni', 'telefono',
            'avatar', 'fecha_nacimiento'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email    = self.cleaned_data['email']
        if self.cleaned_data.get('avatar'):
            user.avatar = self.cleaned_data['avatar']
        if self.cleaned_data.get('fecha_nacimiento'):
            user.fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        if commit:
            user.save()
            Cliente.objects.create(
                usuario           = user,
                nombre            = self.cleaned_data['nombre'],
                apellido          = self.cleaned_data['apellido'],
                dni               = self.cleaned_data['dni'],
                telefono          = self.cleaned_data['telefono'],
                fecha_nacimiento  = self.cleaned_data.get('fecha_nacimiento'),
            )
        return user


class ClientePerfilForm(forms.ModelForm):
    class Meta:
        model  = Cliente
        fields = [
            'nombre', 'apellido', 'dni',
            'telefono', 'fecha_nacimiento'
        ]
        widgets = {
            'nombre':           forms.TextInput(attrs={'class':'form-control'}),
            'apellido':         forms.TextInput(attrs={'class':'form-control'}),
            'dni':              forms.TextInput(attrs={'class':'form-control'}),
            'telefono':         forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type':'date','class':'form-control'}),
        }


class VendedorPerfilForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type':'date','class':'form-control'})
    )

    class Meta:
        model  = Vendedor
        fields = ['email', 'telefono', 'avatar', 'fecha_nacimiento']
        widgets = {
            'email':    forms.EmailInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
        }


class UserEmailForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model  = User
        fields = ['email', 'avatar']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }


class OptionalPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            field.widget.attrs.pop('required', None)
