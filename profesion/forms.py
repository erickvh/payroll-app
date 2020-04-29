from django import forms
import re 
#imports del modelo
from .models import Profesion

def check_number(value):   
    if len(value) < 3:
        raise forms.ValidationError("Minimo requerido de 3")

def check_string(value):   
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if not re.search(regex, value):
        raise forms.ValidationError("Debe ingresar una cadena de texto")

class ProfesionForm(forms.ModelForm):
    nombre = forms.CharField(required=True,validators = [check_number, check_string])
    descripcion = forms.CharField(required=False,validators = [check_number, check_string])

    class Meta:
        model = Profesion
        fields = '__all__'
