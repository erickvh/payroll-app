from django import forms
from datetime import date
#imports del modelo
from .models import Empleado,TipoEmpleadoChoice,TipoIdentificacionChoice
from profesion.models import Profesion
from estado_civil.models import EstadoCivil
from genero.models import Genero
from puesto.models import Puesto
from departamento_organizacion.models import DepartamentoOrganizacion
from municipio.models import Municipio
from departamento.models import Departamento
import re 

def check_number(value):   
    if len(value) < 5:
        raise forms.ValidationError("Minimo requerido de 5")

def check_string(value):   
    regex = '^[A-Za-z_][A-Za-z0-9_]*'
    if not re.search(regex, value):
        raise forms.ValidationError("Debe ingresar una cadena de texto")

def check_direccion(value):   
    if len(value) < 10:
        raise forms.ValidationError("Minimo requerido de 10")

def check_nit(value):
    regex = '^\\d{4}-\\d{6}-\\d{3}-\\d$'
    if not re.search(regex, value):
        raise forms.ValidationError("Ingrese formato correcto de NIT")

def check_nup(value):
    regex = '^\\d{12}'
    if not re.search(regex, value):
        raise forms.ValidationError("Ingrese formato correcto de NUP")

def check_pasaporte(value):
    regex = '^\\d{7}'
    if not re.search(regex, value):
        raise forms.ValidationError("Ingrese formato correcto de Pasaporte")

def check_dui(value):
    regex = '^\\d{8}-\\d$'
    if not re.search(regex, value):
        raise forms.ValidationError("Ingrese formato correcto de DUI")

def check_isss(value):
    regex = '^\\d{9}'
    if not re.search(regex, value):
        raise forms.ValidationError("Ingrese formato correcto de ISSS")

def check_age(born):
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    if age < 18:
        raise forms.ValidationError("Debe tener mas de 18 años")

class EmpleadoForm(forms.ModelForm):
    primer_nombre = forms.CharField(required=True,validators = [check_number, check_string])
    segundo_nombre = forms.CharField(required=True,validators = [check_number, check_string])
    apellido_paterno = forms.CharField(required=True,validators = [check_number, check_string])
    apellido_materno = forms.CharField(required=True,validators = [check_number, check_string])
    apellido_casada = forms.CharField(required=False)
    direccion = forms.CharField(required=True,validators = [check_direccion, check_string])
    identificacion = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(required=True, validators=[check_age])
    isss = forms.CharField(required=True,validators=[check_isss])
    nit = forms.CharField(required=True,validators = [check_nit])
    nup = forms.CharField(required=True,validators = [check_nup])
    salario = forms.FloatField(required=True)
    tipo_empleado = forms.CharField(required=True, 
        widget=forms.Select(attrs={'class' : 'form-control', 'id': 'tipo_empleado'}, choices=[(tag, tag.value) for tag in TipoEmpleadoChoice]))
    tipo_identificacion = forms.CharField(required=True,
        widget=forms.Select(attrs={'class' : 'form-control', 'id': 'tipo_identificacion'},choices=[(tag, tag.value) for tag in TipoIdentificacionChoice]))
    #llaves foraneas
    departamento_organizacion = forms.IntegerField()
    dirigido = forms.IntegerField(required=False)
    estado_civil = forms.IntegerField()
    genero = forms.IntegerField()
    puesto = forms.IntegerField()
    municipio = forms.IntegerField()
    departamento = forms.IntegerField()

    class Meta:
        model = Empleado
        fields = '__all__'
        #exclude = ['tipo_empleado','tipo_identificacion']

    def clean(self):
        cleaned_data = super().clean()
        tipo_identificacion = cleaned_data.get("tipo_identificacion")
        tipo_empleado = cleaned_data.get("tipo_empleado")
        identificacion = cleaned_data.get("identificacion")
        salario = cleaned_data.get("salario")
        puesto = cleaned_data.get("puesto")
        

        if tipo_identificacion and identificacion:
            if tipo_identificacion == 'TipoIdentificacionChoice.DU':
                regex = '^\\d{8}-\\d$'
                if not re.search(regex, identificacion):
                    msg = "Ingrese formato correcto de DUI"
                    self.add_error('identificacion', msg)
            elif tipo_identificacion == 'TipoIdentificacionChoice.PA':
                regex = '^\\d{7}'
                if not re.search(regex, identificacion):
                    msg = "Ingrese formato correcto de Pasaporte"
                    self.add_error('identificacion', msg)
            else:
                msg = "No existe el tipo de identificacion"
                self.add_error('tipo_identificacion', msg)
        
        if salario and puesto:
            if(salario < puesto.minimo or salario > puesto.maximo):
                msg = "Salario debe estar en el rango entre {} y {} del puesto {}".format(puesto.minimo,puesto.maximo, puesto.nombre)
                self.add_error('salario', msg)

        if tipo_empleado:
            if (tipo_empleado != 'TipoEmpleadoChoice.EA' and tipo_empleado != 'TipoEmpleadoChoice.EC'):
                msg = "No existe el tipo de empleado"
                self.add_error('tipo_empleado', msg)


    def clean_estado_civil(self):
        estado_civil_id=self.cleaned_data['estado_civil']
        if EstadoCivil.objects.filter(id=estado_civil_id).exists():
            estado_civil = EstadoCivil.objects.get(id=estado_civil_id)
        else:
            raise forms.ValidationError("Estado Civil Invalido") 

        return estado_civil

    def clean_genero(self):
        genero_id=self.cleaned_data['genero']
        if Genero.objects.filter(id=genero_id).exists():
            genero = Genero.objects.get(id=genero_id)
        else:
            raise forms.ValidationError("Genero Invalido") 

        return genero

    def clean_puesto(self):
        puesto_id=self.cleaned_data['puesto']
        if Puesto.objects.filter(id=puesto_id).exists():
            puesto = Puesto.objects.get(id=puesto_id)
        else:
            raise forms.ValidationError("Puesto Invalido") 

        return puesto

    def clean_municipio(self):
        municipio_id=self.cleaned_data['municipio']
        if Municipio.objects.filter(id=municipio_id).exists():
            municipio = Municipio.objects.get(id=municipio_id)
        else:
            raise forms.ValidationError("Municipio Invalido") 

        return municipio

    def clean_departamento(self):
        departamento_id=self.cleaned_data['departamento']
        if Departamento.objects.filter(id=departamento_id).exists():
            departamento = Departamento.objects.get(id=departamento_id)
        else:
            raise forms.ValidationError("Departamento Invalido") 

        return departamento


    def clean_departamento_organizacion(self):
        departamento_organizacion_id=self.cleaned_data['departamento_organizacion']
        if DepartamentoOrganizacion.objects.filter(id=departamento_organizacion_id).exists():
            departamento_organizacion = DepartamentoOrganizacion.objects.get(id=departamento_organizacion_id)
        else:
            raise forms.ValidationError("Departamento Organizacional Invalido") 

        return departamento_organizacion

    def clean_dirigido(self):
        dirigido=self.cleaned_data['dirigido']
        if Empleado.objects.filter(id=dirigido).exists():
            dirigido = Empleado.objects.get(id=dirigido)
        else:
            dirigido = None

        return dirigido
