from django import forms
import re 
#imports del modelo
from .models import Comision


def check_number(value):   
    if len(value) < 3:
        raise forms.ValidationError("Minimo requerido de 3")

def check_string(value):   
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if not re.search(regex, value):
        raise forms.ValidationError("Debe ingresar una cadena de texto")

class ComisionForm(forms.ModelForm):
    descripcion = forms.CharField(required=False,validators = [check_number, check_string])
    minimo = forms.FloatField(required=True)
    maximo = forms.FloatField(required=True)
    porcentaje = forms.IntegerField(required=True)

    class Meta:
        model = Comision
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        minimo = cleaned_data.get("minimo")
        maximo = cleaned_data.get("maximo")

        if maximo and minimo :
            if(maximo < minimo):
                msg = "El Salario Maximo debe ser mayor al minimo ingresado para el puesto"
                self.add_error('maximo', msg)
        
