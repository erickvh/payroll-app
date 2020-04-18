from django.db import models

# Create your models here.
class Puesto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200,null=True)
    minimo = models.DecimalField(max_digits=8,decimal_places=2)
    maximo = models.DecimalField(max_digits=8,decimal_places=2)

    class Meta:
        db_table = "puestos"

    def __str__(self):
        return self.nombre