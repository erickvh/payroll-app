from django import forms
#imports del modelo
from .models import Genero

class GeneroForm(forms.ModelForm):
    nombre = forms.CharField(required=True)
    class Meta:
        model = Genero
        fields = '__all__'
