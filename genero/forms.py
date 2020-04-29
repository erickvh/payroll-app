from django import forms
# imports del modelo
from .models import Genero
import re 
  
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("Minimo requerido de 3")

        return nombre
