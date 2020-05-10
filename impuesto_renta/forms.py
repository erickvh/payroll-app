from django import forms
import re 
from enum import Enum
#imports del modelo
from .models import ImpuestoRenta

class RentaForm(forms.ModelForm):
    minimo = forms.FloatField(required=True)
    maximo = forms.FloatField(required=True)
    cuota_fija = forms.FloatField(required=True)
    exceso = forms.FloatField(required=True)
    porcentaje = forms.IntegerField(required=True)
    tramo = forms.CharField(required=True)
    periocidad = forms.CharField(required=True)

    class Meta:
        model = ImpuestoRenta
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        minimo = cleaned_data.get("minimo")
        maximo = cleaned_data.get("maximo")

        if maximo and minimo :
            if(maximo < minimo):
                msg = "El Salario Maximo debe ser mayor al minimo ingresado para el puesto"
                self.add_error('maximo', msg)
        
