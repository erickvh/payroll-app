from django.db import models

# Create your models here.
class DepartamentoOrganizacion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "departamento_organizacion"

    def __str__(self):
        return self.nombre