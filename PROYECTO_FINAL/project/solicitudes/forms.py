from django import forms
from .models import Solicitudes

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = ['titulo','descripcion','fecha_de_registro','estatus']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        descripcion = cleaned_data.get('descripcion')
        
        

        if not titulo or not descripcion:
            raise forms.ValidationError('Todos los campos deben de estar completos')
        return cleaned_data