from django import forms
#imports del modelo
from .models import TipoUnidad

class TipoUnidadForm(forms.ModelForm):
    nombre = forms.CharField(required=True)
    descripcion = forms.CharField(required=False)
    class Meta:
        model = TipoUnidad
        fields = '__all__'
