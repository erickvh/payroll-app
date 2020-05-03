from django import forms
#imports del modelo
from .models import Unidad
from tipo_unidad.models import TipoUnidad
from departamento_organizacion.models import DepartamentoOrganizacion
import re 

def check_number(value):   
    if len(value) < 3:
        raise forms.ValidationError("Minimo requerido de 3")

def check_string(value):   
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if not re.search(regex, value):
        raise forms.ValidationError("Debe ingresar una cadena de texto")

class UnidadForm(forms.ModelForm):
    nombre = forms.CharField(required=True,validators = [check_number, check_string])
    tipo_unidad = forms.IntegerField()
    departamento_organizacion = forms.IntegerField()
    dirigido = forms.IntegerField(required=False)

    class Meta:
        model = Unidad
        fields = '__all__'

    def clean_tipo_unidad(self):
        tipo_unidad_id=self.cleaned_data['tipo_unidad']
        if TipoUnidad.objects.filter(id=tipo_unidad_id).exists():
            tipo_unidad = TipoUnidad.objects.get(id=tipo_unidad_id)
        else:
            raise forms.ValidationError("Tipo Unidad Invalido") 

        return tipo_unidad

    def clean_departamento_organizacion(self):
        departamento_organizacion_id=self.cleaned_data['departamento_organizacion']
        if DepartamentoOrganizacion.objects.filter(id=departamento_organizacion_id).exists():
            departamento_organizacion = DepartamentoOrganizacion.objects.get(id=departamento_organizacion_id)
        else:
            raise forms.ValidationError("Departamento Organizacional Invalido") 

        return departamento_organizacion

    def clean_dirigido(self):
        dirigido=self.cleaned_data['dirigido']
        if Unidad.objects.filter(id=dirigido).exists():
            dirigido = Unidad.objects.get(id=dirigido)
        else:
            dirigido = None

        return dirigido