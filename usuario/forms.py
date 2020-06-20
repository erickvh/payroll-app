from django import forms
#imports del modelo
# from .models import DepartamentoOrganizacion
import re 
from usuario.models import User
from django.core.validators import validate_email
from empleado.models import Empleado

def check_number(value):   
    if len(value) < 8:
        raise forms.ValidationError("Minimo requerido de 8")

def check_string(value):   
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if not re.search(regex, value):
        raise forms.ValidationError("Debe ingresar una cadena de texto")

class UserForm(forms.ModelForm):
    username = forms.CharField(required=True,validators = [check_string])
    password= forms.CharField(required=True)
    new_password= forms.CharField(required=True)
    email= forms.CharField(required=True,validators=[validate_email])
    empleado= forms.CharField(required=False)
    is_admin=forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = '__all__'
        exclude=['first_name','last_name','is_staff','is_active','date_joined']

    def clean(self):
        new_password=self.cleaned_data.get('new_password')
        current_password=self.cleaned_data.get('password')
        
        if new_password and not current_password:
            self.add_error('password','Debe colocar el campo password')
        if not new_password and current_password:
            self.add_error('new_password','Debe confirmar contraseña')
        
        if new_password and current_password:
            if not new_password == current_password:
                self.add_error('new_password','No coinciden ambos passwords')
        
    def clean_username(self):
        username= self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario ya existe')
        return username
    
    def clean_is_admin(self):
        admin=self.cleaned_data['is_admin']
        print(admin)
        if not admin:
            is_admin=False
        else:
            is_admin=True

        return is_admin


    def clean_empleado(self):
        empleado_id=self.cleaned_data['empleado']
        if not empleado_id:
            return None

        if Empleado.objects.filter(id=empleado_id).exists():
            if not User.objects.filter(empleado_id=empleado_id).exists():
                empleado = Empleado.objects.get(id=empleado_id)
            else:
                raise forms.ValidationError("Empleado con usuario registrado") 

        else:
            raise forms.ValidationError("Empleado Invalido") 


        return empleado
    
class UserUpdateForm(forms.Form):
    password= forms.CharField(required=False)
    new_password= forms.CharField(required=False)
    email= forms.CharField(required=True,validators=[validate_email])
    is_admin=forms.BooleanField(required=False)



    def clean(self):
        new_password=self.cleaned_data.get('new_password')
        current_password=self.cleaned_data.get('password')

        if new_password and not current_password:
            self.add_error('password','Debe colocar el campo password')
        if not new_password and current_password:
            self.add_error('new_password','Debe confirmar contraseña')

        if new_password and current_password:
            if not new_password == current_password:
                self.add_error('new_password','No coinciden ambos passwords')

    
    def clean_is_admin(self):
        admin=self.cleaned_data['is_admin']
        print(admin)
        if not admin:
            is_admin=False
        else:
            is_admin=True

        return is_admin

    def clean_password(self):
        pswd=self.cleaned_data.get('password')
        if pswd:
            return pswd
        else:
            return None

