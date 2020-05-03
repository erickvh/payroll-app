from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import DepartamentoOrganizacion
from .forms import DepartamentoOrganizacionForm

# Create your views here.
def index_departamento_organizacion(request):
    departamento_organizacion_list = DepartamentoOrganizacion.objects.all().order_by('nombre')
    return render(request, 'departamento_organizacion/index.html', {'departamento_organizacion_list': departamento_organizacion_list})


def create_departamento_organizacion(request):
    return render(request, 'departamento_organizacion/create.html')

def store_departamento_organizacion(request):
    if request.method == 'POST':
        form = DepartamentoOrganizacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento Organizacional Guardado correctamente')
        else:
            errors=form.errors
            data=form.data
            return render(request, 'departamento_organizacion/create.html',{'errors': errors,'data': data})
    return redirect('/departamento_organizacion')

def edit_departamento_organizacion(request, departamento_id):
    departamento_organizacion = get_object_or_404(DepartamentoOrganizacion,pk=departamento_id)
    return render(request, 'departamento_organizacion/edit.html', {'departamento_organizacion': departamento_organizacion})

def update_departamento_organizacion(request, departamento_id):
    departamento_organizacion = get_object_or_404(DepartamentoOrganizacion,pk=departamento_id)
    if request.method == 'POST':
        form = DepartamentoOrganizacionForm(request.POST, instance=departamento_organizacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento Organizacional Actualizado correctamente')
        else:
            errors=form.errors
            return render(request, 'departamento_organizacion/edit.html',{'errors': errors, 'departamento_organizacion':departamento_organizacion})

    return redirect('/departamento_organizacion')

def delete_departamento_organizacion(request, departamento_id):
    departamento_organizacion = get_object_or_404(DepartamentoOrganizacion,pk=departamento_id)
    try:
        departamento_organizacion.delete()
        messages.success(request, 'Departamento Organizacional Borrado correctamente')
    except:
        messages.error(request, 'Este Departamento tiene Unidades asignadas')

    return redirect('/departamento_organizacion')



