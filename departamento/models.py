from django.db import models

# Create your models here.
class Departamento(models.Model):
    codigo = models.CharField(max_length=10, unique=True )
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = "departamentos"

    def __str__(self):
        return self.nombre