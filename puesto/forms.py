from django import forms
#imports del modelo
from .models import Puesto

class PuestoForm(forms.ModelForm):
    nombre = forms.CharField(required=True)
    descripcion = forms.CharField(required=False)
    minimo = forms.FloatField(required=True)
    maximo = forms.FloatField(required=True)

    class Meta:
        model = Puesto
        fields = '__all__'
