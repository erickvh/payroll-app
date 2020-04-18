from django.db import models

# Create your models here.
class Profesion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = "profesiones"

    def __str__(self):
        return self.nombre
    

