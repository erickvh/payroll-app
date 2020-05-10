from django.db import models

# Create your models here.
class Comision(models.Model):
    porcentaje = models.IntegerField()
    minimo = models.DecimalField(max_digits=8,decimal_places=2)
    maximo = models.DecimalField(max_digits=8,decimal_places=2)
    descripcion = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = "comisiones"

    def __str__(self):
        return self.porcentaje