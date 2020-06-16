from django import forms
from datetime import date
from .models import CatalogoDescuento, CatalogoIngreso
import re

def check_string(value):   
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if not re.search(regex, value):
        raise forms.ValidationError("Debe ingresar una cadena de texto")


class DescuentoForm(forms.ModelForm):
    nombre = forms.CharField(required=True,validators = [check_string])
    fecha_inicio = forms.DateField(required=True)
    fecha_fin = forms.DateField(required=True)
    descuento_total = forms.FloatField(required=True)
    cantidad_descontada = forms.FloatField(required=False)
    descuento = forms.FloatField(required=True)
    fijo = forms.BooleanField(required=False,widget=forms.Select(attrs={'class' : 'form-control', 'id': 'fijo'}, choices=[(True, 'Cantidad'),(False, 'Porcentaje')]))

    class Meta:
        model = CatalogoDescuento
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")
        descuento = cleaned_data.get("descuento")
        descuento_total = cleaned_data.get("descuento_total")
        fijo = cleaned_data.get("fijo")
        
        if fecha_inicio and fecha_fin:
            if fecha_inicio >= fecha_fin:
                msg = "La fecha de finalizacion debe ser superior a la fecha de inicio"
                self.add_error('fecha_inicio', msg)
        
        if descuento and descuento_total:
            if fijo:
                if descuento > descuento_total:
                    msg = "El descuento que pretende es superior al monto total"
                    self.add_error('descuento', msg)
            else:
                if descuento > 50:
                    msg = "No puede descontar mas del 50%"
                    self.add_error('descuento', msg)


class IngresoForm(forms.ModelForm):
    nombre = forms.CharField(required=True,validators = [check_string])
    fecha_inicio = forms.DateField(required=True)
    fecha_fin = forms.DateField(required=True)
    ingreso = forms.FloatField(required=True)
    porcentaje = forms.FloatField(required=False)
    comision = forms.BooleanField(required=False,widget=forms.Select(attrs={'class' : 'form-control', 'id': 'fijo'}, choices=[(True, 'Comision'),(False, 'Otros')]))

    class Meta:
        model = CatalogoIngreso
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")
        
        if fecha_inicio and fecha_fin:
            if fecha_inicio >= fecha_fin:
                msg = "La fecha de finalizacion debe ser superior a la fecha de inicio"
                self.add_error('fecha_inicio', msg)
        



