from django.db import models

# Create your models here.
class TipoUnidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = "tipo_unidad"

    def __str__(self):
        return self.nombre