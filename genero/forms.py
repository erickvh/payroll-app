from django import forms
# imports del modelo
from .models import Genero
import re 

def check_number(value):   
    if len(value) < 3:
        raise forms.ValidationError("Minimo requerido de 3")

def check_string(value):   
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if not re.search(regex, value):
        raise forms.ValidationError("Debe ingresar una cadena de texto")

class GeneroForm(forms.ModelForm):
    nombre = forms.CharField(required=True,validators = [check_number, check_string])
    
    class Meta:
        model = Genero
        fields = '__all__'
    

    
