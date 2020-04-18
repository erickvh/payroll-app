from django.db import models

# Create your models here.
class Configuracion(models.Model):
    nombre = models.CharField(max_length=50)
    sociedad = models.CharField(max_length=100, null=True)
    representante_legal = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=200,null=True)
    telefono= models.CharField(max_length=10, null=True)
    web= models.CharField(max_length=50, null=True)
    nic= models.CharField(max_length=20, null=True)
    nit= models.CharField(max_length=20, null=True)
    direccion = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    salario_minimo_sector = models.DecimalField(max_digits=8,decimal_places=2)

    class Meta:
        db_table = "configuracion"

    def __str__(self):
        return self.nombre