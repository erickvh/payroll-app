from django.shortcuts import render
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from .models import * 
from datetime import datetime as today

# Descuentos de ley
def descuento_ley(request):
    descuentos = DescuentoGeneral.objects.all()
    return render(request, "descuento_general/descuento_ley.html",{'descuentos':descuentos})

def crear_descuento(request):
    if request.method == 'POST':
        descuento = request.POST.get('descuento', None)
        porcentaje = int(request.POST.get('porcentaje', None))
        if descuento and porcentaje:
            if porcentaje>0 and porcentaje <100:
                descuento_general = DescuentoGeneral(nombre = descuento, porcentaje=round(int(porcentaje)/100,2))
                descuento_general.save()
                messages.success(request, 'Descuento creado con exito')
            else:
                messages.error(request, 'Error, porcentaje debe estar entre 1 y el 99%')
        else:
            messages.error(request, 'Error, debe llenar los datos para crear un nuevo descuento de ley')
    return redirect("/descuento/")

def edit_descuento(request):
    if request.method == 'POST':
        descuento = request.POST.get('edit_descuento', None)
        porcentaje = int(request.POST.get('edit_porcentaje', 0))
        descuento_id = int(request.POST.get('edit_id', 0))
        if descuento and porcentaje:
            if porcentaje>0 and porcentaje <100:
                descuento_general = get_object_or_404(DescuentoGeneral,pk=descuento_id)
                descuento_general.nombre = descuento
                descuento_general.porcentaje = round(int(porcentaje)/100,2)
                descuento_general.save()
                messages.success(request, 'Descuento editado con exito')
            else:
                messages.error(request, 'Error, porcentaje debe estar entre 1 y el 99%')
        else:
            messages.error(request, 'Error, debe llenar los datos para crear un nuevo descuento de ley')
    return redirect("/descuento/")


def cerrar_descuento(request, descuento_id):
    if request.method == 'POST':
        descuento_general = get_object_or_404(DescuentoGeneral,pk=descuento_id)
        descuento_general.activo = not descuento_general.activo
        descuento_general.save()
        messages.success(request, 'Cambio exitoso')
    else:
        messages.error(request, 'Error, metodo no valido, tiene que ser un metodo post')
    return redirect("/descuento/")


#Periodicidad


def periodicidad(request):
    periodos = Periodicidad.objects.all()
    return render(request, "periodicidad/periodicidad.html",{'periodos':periodos})

def crear_periodo(request):
    periodos = Periodicidad.objects.filter(activo=True)
    if len(periodos)>0:
        messages.error(request, 'Error, debe cerrar todos los periodos')
        return redirect('/general/periodicidad')

    if request.method == 'POST':
        periodicidad = int(request.POST.get('periodicidad',None))
        last_periodo = Periodicidad.objects.all().last()
        if last_periodo.anio_periodo == today.now().year:
            messages.error(request, 'Error, no deberias poder crear otro periodo, pero para fines de pruebas se le permite')
        if periodicidad:
            periodo = Periodicidad(anio_periodo=today.now().year)
            if periodicidad == 2:
                periodo.mensual = False
            periodo.save()
        else:
            messages.error(request, 'Error, debe llenar los datos solicitados')
    else:
        messages.error(request, 'Error, debe llenar los datos')
    return redirect("/general/periodicidad")

def cerrar_periodo(request, periodo_id):
    if request.method == 'POST':
        periodo = get_object_or_404(Periodicidad,pk=periodo_id)
        periodo.activo = False
        periodo.save()
        messages.success(request, 'Cierre exitoso')
    else:
        messages.error(request, 'Error, metodo no valido, tiene que ser un metodo post')
    return redirect("/general/periodicidad")


