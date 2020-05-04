from django import forms
# imports del modelo
from .models import CentroCostos
from departamento_organizacion.models import DepartamentoOrganizacion
import re


def check_presupuesto(value):
    if value < 0:
        raise forms.ValidationError("El presupuesto debe ser mayor a 0")


def check_remanente(value):
    if value < 0:
        raise forms.ValidationError("El remanente debe ser mayor a 0")


class CentroCostosForm(forms.ModelForm):
    presupuesto = forms.FloatField(required=True, validators=[check_presupuesto])
    fecha_inicio = forms.DateField(required=True)
    fecha_fin = forms.DateField(required=True)
    remanente = forms.FloatField(required=True, validators=[check_remanente])
    departamento_organizacion = forms.IntegerField()

    class Meta:
        model = CentroCostos
        fields = '__all__'

    def clean_departamento_organizacion(self):
        departamento_id = self.cleaned_data['departamento_organizacion']
        if DepartamentoOrganizacion.objects.filter(id=departamento_id).exists():
            departamento_organizacion = DepartamentoOrganizacion.objects.get(id=departamento_id)
        else:
            raise forms.ValidationError("Departamento no valido")

        return departamento_organizacion

    def clean_fecha_fin(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio', '')
        fecha_fin = self.cleaned_data.get('fecha_fin', '')
        if str(fecha_inicio) > str(fecha_fin):
            raise forms.ValidationError("La fecha de finalizacion debe ser mayor a la fecha de inicio")
        return fecha_fin
