from django.shortcuts import render
from .models import Planilla, DescuentoGeneral
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from datetime import date
from django.db import connection


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
    planilla.codigo = planilla.codigo + str(planilla.id)
    planilla.save()
    return redirect('/planilla/')

def show_planilla(request, planilla_id):
    planilla = get_object_or_404(Planilla,pk=planilla_id)
    if planilla.activa == False:
        return render(request, 'planilla/show.html', {'planilla': planilla})
    else: 
        descuento_general = DescuentoGeneral.objects.all()
        cabeceras = ["id","salario", "primer_nombre","apellido_paterno","otros_ingresos", "comision", "descuento","total",]
        cuerpo = []
        for d in descuento_general:
            cabeceras.append(d.nombre)
        cursor = connection.cursor()
        cursor.execute("select 	e.id, e.salario, e.primer_nombre,e.apellido_paterno, get_ingreso_total_de_catalogo(e.id), get_ingreso_total_comision(e.id) , get_descuento_total(e.id), (e.salario - get_descuento_total(e.id) + get_ingreso_total_comision(e.id) + get_ingreso_total_de_catalogo(e.id)) from empleados as e;") 
        for row in cursor.fetchall():
            lista = list(row)
            for d in descuento_general:
                lista.append(round(d.porcentaje*lista[1], 2))
            cuerpo.append(lista)
        return render(request, 'planilla/show.html', {'cabeceras': cabeceras, 'cuerpo':cuerpo})




