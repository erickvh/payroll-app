from django.db import models

# Create your models here.

# Tablas sin relaciones

class SalarioMinimo(models.Model):
    monto = models.DecimalField(max_digits=8,decimal_places=2)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "salario_minimo"

    def __str__(self):
        return "salario minimo de {}".format(self.monto)

class Periodicidad(models.Model):
    anio_periodo = models.IntegerField()
    quincenal = models.BooleanField(default=False)
    mensual = models.BooleanField(default=True)

    class Meta:
        db_table = "periodicidad"

    def __str__(self):
        return "Peridiocidad {}".format("mensual" if self.mensual else "quincenal")

    

class DescuentoGeneral(models.Model):
    nombre = models.TextField(max_length=75)
    porcentaje = models.DecimalField(max_digits=8,decimal_places=2)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = "descuento_general"

    def __str__(self):
        return self.nombre

