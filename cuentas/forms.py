from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from .models import Vendedor, Cliente

User = get_user_model()


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )


class ClienteRegistroForm(UserCreationForm):
    email    = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    nombre   = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    dni      = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    avatar   = forms.ImageField(required=False)

    class Meta:
        model  = Vendedor
        fields = ['email', 'password1', 'password2','nombre', 'apellido', 'dni', 'telefono', 'avatar']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email    = self.cleaned_data['email']
        if self.cleaned_data.get('avatar'):
            user.avatar = self.cleaned_data['avatar']
        if commit:
            user.save()
            Cliente.objects.create(
                usuario=user,
                nombre   = self.cleaned_data['nombre'],
                apellido = self.cleaned_data['apellido'],
                dni      = self.cleaned_data['dni'],
                telefono = self.cleaned_data['telefono']
            )
        return user


class ClientePerfilForm(forms.ModelForm):
    class Meta:
        model  = Cliente
        fields = ['nombre', 'apellido', 'dni', 'telefono']
        widgets = {
            'nombre':   forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'dni':      forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
        }


class VendedorPerfilForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model  = Vendedor
        fields = ['email', 'telefono', 'avatar']
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