from django import forms
#imports del modelo
from .models import Configuracion

class ConfiguracionForm(forms.ModelForm):
    nombre = forms.CharField(required=True)
    sociedad = forms.CharField(required=False)
    representante_legal = forms.CharField(required=False)
    descripcion = forms.CharField(required=False)
    telefono = forms.CharField(required=False)
    web = forms.CharField(required=False)
    nic = forms.CharField(required=False)
    nit = forms.CharField(required=False)
    direccion = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    salario_minimo_sector = forms.FloatField(required=True)

    class Meta:
        model = Configuracion
        fields = '__all__'
