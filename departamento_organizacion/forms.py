from django import forms
#imports del modelo
from .models import DepartamentoOrganizacion
import re 

def check_number(value):   
    if len(value) < 1:
        raise forms.ValidationError("Minimo requerido de 3")

def check_string(value):   
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if not re.search(regex, value):
        raise forms.ValidationError("Debe ingresar una cadena de texto")

class DepartamentoOrganizacionForm(forms.ModelForm):
    nombre = forms.CharField(required=True,validators = [check_number, check_string])

    class Meta:
        model = DepartamentoOrganizacion
        fields = '__all__'