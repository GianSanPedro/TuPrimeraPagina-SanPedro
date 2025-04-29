# concesionaria/forms.py

from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model  = Vehiculo
        fields = ['marca','modelo','tipo','año','precio','disponible','foto',]
        widgets = {'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),}
