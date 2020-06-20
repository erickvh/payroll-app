from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from empleado.models import Empleado
# Create your models here.
class User(AbstractUser):
    empleado = models.OneToOneField(Empleado,on_delete=models.PROTECT, null=True)
    class Meta:
        db_table = "usuarios"


class Menu(models.Model):
    nombre = models.TextField(max_length=75)
    url = models.TextField(max_length=75, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    padre = models.ForeignKey('self', null=True, related_name='menu', related_query_name='menu',on_delete=models.PROTECT)

    class Meta:
        db_table = "menu"

    def __str__(self):
        return self.nombre

