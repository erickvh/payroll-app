from django import forms
#imports del modelo
from .models import Municipio
from departamento.models import Departamento
import re 

def check_number(value):   
    if len(value) < 3:
        raise forms.ValidationError("Minimo requerido de 3")

def check_string(value):   
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if not re.search(regex, value):
        raise forms.ValidationError("Debe ingresar una cadena de texto")

class MunicipioForm(forms.ModelForm):
    codigo = forms.CharField(required=True,validators = [check_number])
    nombre = forms.CharField(required=True,validators = [check_number, check_string])
    departamento = forms.IntegerField()

    class Meta:
        model = Municipio
        fields = '__all__'

    def clean_departamento(self):
        departamento_id=self.cleaned_data['departamento']
        if Departamento.objects.filter(id=departamento_id).exists():
            departamento = Departamento.objects.get(id=departamento_id)
        else:
            raise forms.ValidationError("Departamento Invalido") 

        return departamento
  


