from django.db import models
from django.contrib.auth.models import AbstractUser
from empleado.models import Empleado
# Create your models here.
class User(AbstractUser):
    empleado = models.OneToOneField(Empleado,on_delete=models.PROTECT, null=True)
    class Meta:
        db_table = "usuarios"