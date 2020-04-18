from django import forms
#imports del modelo
from .models import Profesion

class ProfesionForm(forms.ModelForm):
    nombre = forms.CharField(required=True)
    descripcion = forms.CharField(required=False)
    class Meta:
        model = Profesion
        fields = '__all__'
