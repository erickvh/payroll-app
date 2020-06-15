from django.shortcuts import render
from .models import *
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
    cabeceras = ["ID","Primer_nombre","Apellido_paterno","Salario","Otros_ingresos", "Comision" ,"Renta", "Descuento total","Total","Accion"]
    cuerpo = []
    for d in descuento_general:
        cabeceras.insert(6, d.nombre)
    cursor = connection.cursor()
    cursor.execute("SELECT id, primer_nombre, apellido_paterno, salario_actual, total_ingreso, total_comision, renta ,total_descuento ,total FROM vista_planilla where planilla_id = "+str(planilla.id)) 
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
    comision = False
    if "Choice.EC" in empleado.tipo_empleado:
        comision = True
    periodicidad = Periodicidad.objects.all().last()
    descuento = DescuentoEmpleado.objects.filter(planilla_id=planilla.id, empleado_id = empleado.id)
    ingreso = IngresoEmpleado.objects.filter(planilla_id=planilla.id, empleado_id = empleado.id)

    cursor = connection.cursor()
    cursor.execute("SELECT total, renta, total_descuento FROM vista_planilla where planilla_id = "+str(planilla.id) +" and id = "+str(empleado.id)) 
    total = 0
    renta = 0
    total_descuento = 0
    for row in cursor.fetchall():
        total += row[0]
        renta += row[1]
        total_descuento += row[2]
    descuento_activo = CatalogoDescuento.objects.all()
    ingreso_activo = CatalogoIngreso.objects.all()
    context = {
        'empleado':empleado, 
        "boleta":boleta, 
        "periodicidad":periodicidad, 
        "fecha":date.today, 
        "comision":comision, 
        "descuentos":descuento, 
        "ingresos":ingreso, 
        "total":total,
        "renta":renta,
        "total_descuento":total_descuento,
        "activa":planilla.activa,
        "descuento_activo":descuento_activo,
        "ingreso_activo":ingreso_activo,
        "planilla_id":planilla.id,
    }
    return render(request, 'planilla/boleta.html', context)

def nuevo_descuento(request):
    if request.method == 'POST':
        print("metodo post")
        planilla = request.POST.get("planilla", None)
        empleado = request.POST.get("empleado", None)
        descuento = request.POST.get("descuento", None)
        if planilla == None and empleado == None and descuento == None:
            print("todo none")
            return redirect("/planilla/")
        elif descuento == None or int(descuento) < 1: 
            print("descuento none")
            messages.error(request, 'Error, debe seleccionar un descuento que aplicar')
            return redirect("/planilla/"+str(empleado)+"/"+str(planilla)+"/boleta")
        else: 
            descuento = int(descuento)
            planilla = get_object_or_404(Planilla,pk=planilla)
            empleado = get_object_or_404(Empleado,pk=empleado)
            descuento = get_object_or_404(CatalogoDescuento,pk=descuento)            
            descuento_empleado = DescuentoEmpleado(activo=True,empleado = empleado, planilla = planilla, descuento=descuento)
            descuento_empleado.save()
            return redirect("/planilla/"+str(empleado.id)+"/"+str(planilla.id)+"/boleta")
    else: 
        print("metodo get")
        return redirect("/planilla/")

def delete_descuento(request, descuento_id):
    print("borrando descuento")
    planilla = request.POST.get("planilla", None)
    empleado = request.POST.get("empleado", None)
    descuento = get_object_or_404(DescuentoEmpleado,pk=descuento_id)
    descuento.delete()
    return redirect("/planilla/"+str(empleado)+"/"+str(planilla)+"/boleta")



def nuevo_ingreso(request):
    if request.method == 'POST':
        print("metodo post")
        planilla = request.POST.get("planilla", None)
        empleado = request.POST.get("empleado", None)
        ingreso = request.POST.get("ingreso", None)
        if planilla == None and empleado == None and ingreso == None:
            print("todo none")
            return redirect("/planilla/")
        elif ingreso == None or int(ingreso) < 1: 
            print("descuento none")
            messages.error(request, 'Error, debe seleccionar un ingreso que aplicar')
            return redirect("/planilla/"+str(empleado)+"/"+str(planilla)+"/boleta")
        else: 
            ingreso = int(ingreso)
            planilla = get_object_or_404(Planilla,pk=planilla)
            empleado = get_object_or_404(Empleado,pk=empleado)
            ingreso = get_object_or_404(CatalogoIngreso,pk=ingreso)            
            ingreso_empleado = IngresoEmpleado(activo=True,empleado = empleado, planilla = planilla, ingreso=ingreso)
            ingreso_empleado.save()
            return redirect("/planilla/"+str(empleado.id)+"/"+str(planilla.id)+"/boleta")
    else: 
        print("metodo get")
        return redirect("/planilla/")


def delete_ingreso(request, ingreso_id):
    print("borrando descuento")
    planilla = request.POST.get("planilla", None)
    empleado = request.POST.get("empleado", None)
    ingreso = get_object_or_404(IngresoEmpleado,pk=ingreso_id)
    ingreso.delete()
    return redirect("/planilla/"+str(empleado)+"/"+str(planilla)+"/boleta")




