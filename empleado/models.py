from django.db import models
from enum import Enum
from profesion.models import Profesion
from estado_civil.models import EstadoCivil
from genero.models import Genero
from puesto.models import Puesto
from departamento_organizacion.models import DepartamentoOrganizacion
from municipio.models import Municipio

# Create your models here.
class TipoEmpleadoChoice(Enum):   # A subclass of Enum
    EA = "Empleado Administrativo"
    EC = "Empleado con Comisión"

class TipoIdentificacionChoice(Enum):   # A subclass of Enum
    DU = "DUI"
    PA = "Pasaporte"

class Empleado(models.Model):
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    apellido_casada = models.CharField(max_length=25,null=True)
    direccion = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=30,unique=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    isss = models.CharField(max_length=30,unique=True)
    nup = models.CharField(max_length=30,unique=True)
    nit = models.CharField(max_length=30,unique=True)
    salario = models.DecimalField(max_digits=8,decimal_places=2)
    tipo_empleado = models.CharField(max_length=50)
    tipo_identificacion = models.CharField(max_length=50)
    dirigido = models.ForeignKey('self', null=True, related_name='empleados', related_query_name='empleado',on_delete=models.PROTECT)
    profesion = models.ForeignKey(Profesion,on_delete=models.PROTECT)
    estado_civil = models.ForeignKey(EstadoCivil,on_delete=models.PROTECT)
    genero = models.ForeignKey(Genero,on_delete=models.PROTECT)
    puesto = models.ForeignKey(Puesto,on_delete=models.PROTECT)
    departamento_organizacion = models.ForeignKey(DepartamentoOrganizacion,on_delete=models.PROTECT)
    municipio = models.ForeignKey(Municipio,on_delete=models.PROTECT)
    

    class Meta:
        db_table = "empleados"

    def __str__(self):
        return self.primer_nombre
