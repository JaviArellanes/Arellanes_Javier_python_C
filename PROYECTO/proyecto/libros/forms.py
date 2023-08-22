from django import forms
from .models import Libros

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ['titulo', 'edicion', 'editorial', 'año_publicacion', 'paginas']

        def clean(self):
            cleaned_data = super().clean()
            titulo = cleaned_data.get('titulo')
            edicion = cleaned_data.get('edicion')
            editorial = cleaned_data.get('editorial')
            año_publicacion = cleaned_data.get('año_publicacion')
            paginas = cleaned_data.get('paginas')

            if not titulo or edicion or not editorial or not año_publicacion or not paginas:
                raise forms.ValidationError("Todos los campos deben estar completos")
            
            return cleaned_data