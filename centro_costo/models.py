from django.core.exceptions import ValidationError
from django.db import models
from departamento_organizacion.models import DepartamentoOrganizacion


# Create your models here.

class CentroCostos(models.Model):
    presupuesto = models.FloatField()
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
    remanente = models.FloatField()
    departamento_organizacion = models.ForeignKey(DepartamentoOrganizacion, on_delete=models.PROTECT)

    class Meta:
        db_table = "centro_costos"

    def __str__(self):
        return self.departamento_organizacion.nombre
