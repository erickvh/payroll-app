from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages

from .models import Unidad
from tipo_unidad.models import TipoUnidad
from .forms import UnidadForm

def index_unidad(request):
    unidad_list = Unidad.objects.all().order_by('nombre')
    return render(request, 'unidad/index.html', {'unidad_list': unidad_list})

def create_unidad(request):
    unidad_list = Unidad.objects.all().order_by('nombre')
    tipo_unidad_list = TipoUnidad.objects.all().order_by('nombre')
    context = {'tipo_unidad_list': tipo_unidad_list, 'unidad_list': unidad_list}
    return render(request, 'unidad/create.html',context)
    

def store_unidad(request):
    if request.method == 'POST':
        form = UnidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Unidad Guardada correctamente')
        else:
            errors=form.errors
            data=form.data
            unidad_list = Unidad.objects.all().order_by('nombre')
            tipo_unidad_list = TipoUnidad.objects.all().order_by('nombre')
            context = {'tipo_unidad_list': tipo_unidad_list, 'unidad_list': unidad_list, 'errors': errors, 'data': data}
            return render(request, 'unidad/create.html',context)
           
    return redirect('/unidad')

def edit_unidad(request, unidad_id):
    unidad = get_object_or_404(Unidad,pk=unidad_id)
    unidad_list = Unidad.objects.all().order_by('nombre')
    tipo_unidad_list = TipoUnidad.objects.all().order_by('nombre')
    context = {'unidad': unidad ,'tipo_unidad_list': tipo_unidad_list, 'unidad_list': unidad_list}
    return render(request, 'unidad/edit.html', context)


def update_unidad(request, unidad_id):
    unidad = get_object_or_404(Unidad,pk=unidad_id)
    unidad_list = Unidad.objects.all().order_by('nombre')
    tipo_unidad_list = TipoUnidad.objects.all().order_by('nombre')
    if request.method == 'POST':
        form = UnidadForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Unidad actualizada correctamente')
        else:
            errors=form.errors
            context = {'errors': errors, 'unidad':unidad,'tipo_unidad_list': tipo_unidad_list, 'unidad_list': unidad_list}
            return render(request, 'unidad/edit.html',context)
        
    return redirect('/unidad')


def delete_unidad(request, unidad_id):
    unidad = get_object_or_404(Unidad,pk=unidad_id)
    try:
        unidad.delete()
        messages.success(request, 'Unidad Borrada correctamente')
    except:
        messages.error(request, 'Esta Unidad tiene unidades asignadas')
    return redirect('/unidad')


