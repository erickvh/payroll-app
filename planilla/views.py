from django.shortcuts import render
from .models import Planilla, DescuentoGeneral, BoletaPago
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from datetime import date
from django.db import connection
from empleado.models import Empleado

def home(request):
    planillas = Planilla.objects.all()
    return render(request, 'planilla/home.html', {'planillas': planillas})


def create_planilla(request):
    planillas = Planilla.objects.all().filter(activa=True)
    if len(planillas)>0:
        messages.error(request, 'Error, debe cerrar todas las planillas para crear una nueva')
        return redirect('/planilla/')
    fecha = date.today()
    planilla = Planilla()
    planilla.codigo = "P{}{}".format(fecha.year,fecha.month)
    planilla.fecha = fecha 
    planilla.activa = True
    planilla.save()
    c = ""
    if planilla.id < 10:
        c = "00"
    elif planilla.id > 9 and planilla.id < 100:
        c = "0"
    planilla.codigo = planilla.codigo +  c + str(planilla.id)
    planilla.save()
    return redirect('/planilla/')

def show_planilla(request, planilla_id):
    planilla = get_object_or_404(Planilla,pk=planilla_id)
    descuento_general = DescuentoGeneral.objects.all()
    cabeceras = ["ID","Primer_nombre","Apellido_paterno","Salario","Otros_ingresos", "Comision", "Descuento total","Total","Accion"]
    cuerpo = []
    for d in descuento_general:
        cabeceras.insert(6, d.nombre)
    cursor = connection.cursor()
    cursor.execute("SELECT id, primer_nombre, apellido_paterno, salario_actual, total_ingreso, total_comision, total_descuento, total FROM vista_planilla where planilla_id = "+str(planilla.id)) 
    for row in cursor.fetchall():
        lista = list(row)
        for d in descuento_general:
            lista.insert(6,round(d.porcentaje*lista[3], 2))
        cuerpo.append(lista)
    return render(request, 'planilla/show.html', {'cabeceras': cabeceras, 'cuerpo':cuerpo, 'codigo':planilla.codigo, 'activa':planilla.activa, "planilla_id":planilla.id})


def close_planilla(request, planilla_id):
    planilla = get_object_or_404(Planilla,pk=planilla_id)
    planilla.activa = False
    planilla.save()
    return redirect("/planilla/")


def boleta(request, empleado_id, planilla_id):
    planilla = get_object_or_404(Planilla,pk=planilla_id)
    empleado = get_object_or_404(Empleado,pk=empleado_id)
    boleta = BoletaPago.objects.filter(planilla_id=planilla.id, empleado_id = empleado.id).first()
    return render(request, 'planilla/boleta.html', {'empleado':empleado, "boleta":boleta})


