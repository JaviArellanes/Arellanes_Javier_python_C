from typing import Any, Dict
from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre','descripcion','precio','fecha_de_registro','estatus']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        descripcion = cleaned_data.get('descripcion')
        precio = cleaned_data.get('precio')
        fecha_de_registro = cleaned_data.get('fecha de registro')
        estatus = cleaned_data.get('estatus')

        if not titulo or not descripcion or not precio or not fecha_de_registro or not estatus:
            raise forms.ValidationError('Todos los campos deben de estar completos')
        return cleaned_data