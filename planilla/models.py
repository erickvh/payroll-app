from django.db import models
from empleado.models import Empleado

# Tablas relacionadas, muchas con las tablas de la primera etapa

class Planilla(models.Model):
    codigo = models.TextField(max_length=20)
    fecha = models.DateField()
    total_pago_empleado = models.DecimalField(max_digits=8,decimal_places=2, default = 0.0)
    total_descuento = models.DecimalField(max_digits=8,decimal_places=2, default = 0.0)
    total_pagar = models.DecimalField(max_digits=8,decimal_places=2, default = 0.0)
    activa = models.BooleanField(default=False, blank=True)
    
    class Meta:
        db_table = "planilla"

    def __str__(self):
        return self.codigo

class BoletaPago(models.Model):
    empleado = models.ForeignKey(Empleado,on_delete=models.PROTECT)
    planilla = models.ForeignKey(Planilla, on_delete=models.PROTECT)
    codigo = models.TextField(max_length=20)
    fecha_pago = models.DateField()
    dias_laborales = models.IntegerField(default=23)
    dias_trabajados = models.IntegerField(default=23)
    salario_actual = models.DecimalField(max_digits=8,decimal_places=2, default = 0.0)
    total_comision = models.DecimalField(max_digits=8,decimal_places=2, default = 0)
    total_descuento = models.DecimalField(max_digits=8,decimal_places=2, default = 0)
    total_ingreso = models.DecimalField(max_digits=8,decimal_places=2, default = 0)
    pago_total = models.DecimalField(max_digits=8,decimal_places=2, default = 0)
    pago_neto = models.DecimalField(max_digits=8,decimal_places=2, default = 0)
    activa = models.BooleanField(default=False, blank=True)
    
    class Meta:
        db_table = "boleta_pago"

    def __str__(self):
        return self.codigo



class CatalogoDescuento(models.Model):
    nombre = models.TextField(max_length=75)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descuento_total = models.DecimalField(max_digits=8,decimal_places=2, default=0.0)
    cantidad_descontada = models.DecimalField(max_digits=8,decimal_places=2, default=0.0)
    descuento = models.DecimalField(max_digits=8,decimal_places=2)
    fijo = models.BooleanField(default=False)

    class Meta:
        db_table = "catalogo_descuento"

    def __str__(self):
        return self.nombre

class DescuentoEmpleado(models.Model):
    activo  = models.BooleanField(default=True)
    empleado = models.ForeignKey(Empleado,on_delete=models.PROTECT)
    descuento = models.ForeignKey(CatalogoDescuento, on_delete=models.PROTECT)

    class Meta:
        db_table = "descuento_empleado"

    def __str__(self):
        return self.empleado


class CatalogoIngreso(models.Model):
    nombre = models.TextField(max_length=75)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ingreso = models.DecimalField(max_digits=8,decimal_places=2)
    comision = models.BooleanField(default=False)
    porcentaje = models.DecimalField(max_digits=8,decimal_places=2)

    class Meta:
        db_table = "catalogo_ingreso"

    def __str__(self):
        return self.nombre

class IngresoEmpleado(models.Model):
    activo = models.BooleanField(default=True)
    empleado = models.ForeignKey(Empleado,on_delete=models.PROTECT)
    ingreso = models.ForeignKey(CatalogoIngreso, on_delete=models.PROTECT)

    class Meta:
        db_table = "ingreso_empleado"

    def __str__(self):
        return self.empleado


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



