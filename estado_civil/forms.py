from django import forms
#imports del modelo
from .models import EstadoCivil

class EstadoCivilForm(forms.ModelForm):
    nombre = forms.CharField(required=True)
    descripcion = forms.CharField(required=False)
    class Meta:
        model = EstadoCivil
        fields = '__all__'
