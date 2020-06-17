from django.shortcuts import render
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from .models import * 

# Create your views here.


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


