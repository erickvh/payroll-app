from django.db import models
from departamento.models import Departamento

# Create your models here.
class Municipio(models.Model):
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento,on_delete=models.PROTECT)

    class Meta:
        db_table = "municipios"

    def __str__(self):
        return self.nombre