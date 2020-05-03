from django.db import models
from tipo_unidad.models import TipoUnidad
from departamento_organizacion.models import DepartamentoOrganizacion
# Create your models here.
class Unidad(models.Model):
    nombre = models.CharField(max_length=50)
    dirigido = models.ForeignKey('self', null=True, related_name='dirigidos', related_query_name='unidad',on_delete=models.PROTECT)
    tipo_unidad = models.ForeignKey(TipoUnidad,on_delete=models.PROTECT)
    departamento_organizacion = models.ForeignKey(DepartamentoOrganizacion,on_delete=models.PROTECT)

    class Meta:
        db_table = "unidades"

    def __str__(self):
        return self.nombre