from django.db import models

# Create your models here.
class ImpuestoRenta(models.Model):
    porcentaje = models.IntegerField()
    minimo = models.DecimalField(max_digits=8,decimal_places=2)
    maximo = models.DecimalField(max_digits=8,decimal_places=2)
    exceso = models.DecimalField(max_digits=8,decimal_places=2)
    cuota_fija = models.DecimalField(max_digits=8,decimal_places=2)
    tramo = models.CharField(max_length=100)
    periocidad = models.CharField(max_length=100)

    class Meta:
        db_table = "impuesto_renta"

    def __str__(self):
        return self.tramo