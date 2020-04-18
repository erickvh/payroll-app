from django import forms
#imports del modelo
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    codigo = forms.CharField(required=True)
    nombre = forms.CharField(required=True)
    class Meta:
        model = Departamento
        fields = '__all__'
