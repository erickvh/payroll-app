# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.http import JsonResponse
#imports del modelo
from .models import Empleado,TipoIdentificacionChoice,TipoEmpleadoChoice
from profesion.models import Profesion
from estado_civil.models import EstadoCivil
from genero.models import Genero
from puesto.models import Puesto
from departamento_organizacion.models import DepartamentoOrganizacion
from municipio.models import Municipio
from departamento.models import Departamento
from .forms import EmpleadoForm


# Create your views here.
def index_empleado(request):
    empleado_list = Empleado.objects.all().order_by('primer_nombre')
    return render(request, 'empleado/index.html', {'empleado_list': empleado_list})

def create_empleado(request):
    profesion_list = Profesion.objects.all().order_by('nombre')
    estado_civil_list = EstadoCivil.objects.all().order_by('nombre')
    puesto_list = Puesto.objects.all().order_by('nombre')
    departamento_organizacion_list = DepartamentoOrganizacion.objects.all().order_by('nombre')
    empleado_list = Empleado.objects.all().order_by('primer_nombre')
    genero_list = Genero.objects.all().order_by('nombre')
    municipio_list = Municipio.objects.all().order_by('nombre')
    departamento_list = Departamento.objects.all().order_by('nombre')
    form = EmpleadoForm
    context={
        'departamento_organizacion_list':departamento_organizacion_list, 
        'empleado_list': empleado_list,
        'profesion_list': profesion_list,
        'estado_civil_list': estado_civil_list,
        'puesto_list': puesto_list,
        'municipio_list': municipio_list,
        'genero_list': genero_list,
        'departamento_list': departamento_list,
        'form':form
    }
    return render(request, 'empleado/create.html', context)

def store_empleado(request):
    profesion_list = Profesion.objects.all().order_by('nombre')
    estado_civil_list = EstadoCivil.objects.all().order_by('nombre')
    puesto_list = Puesto.objects.all().order_by('nombre')
    departamento_organizacion_list = DepartamentoOrganizacion.objects.all().order_by('nombre')
    empleado_list = Empleado.objects.all().order_by('primer_nombre')
    genero_list = Genero.objects.all().order_by('nombre')
    municipio_list = Municipio.objects.all().order_by('nombre')
    departamento_list = Departamento.objects.all().order_by('nombre')
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado Guardado correctamente')
        else:
            errors=form.errors
            data=form.data
            context={
                'departamento_organizacion_list':departamento_organizacion_list, 
                'empleado_list': empleado_list,
                'profesion_list': profesion_list,
                'estado_civil_list': estado_civil_list,
                'puesto_list': puesto_list,
                'municipio_list': municipio_list,
                'genero_list': genero_list,
                'departamento_list': departamento_list,
                'errors': errors, 
                'data': data,
                'form':form
            }
            return render(request, 'empleado/create.html',context)
           
    return redirect('/empleado')
"""
def edit_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento,pk=departamento_id)
    context = {'departamento': departamento}
    return render(request, 'departamento/edit.html', context)
   
def update_departamento(request, departamento_id):
    departamento =  get_object_or_404(Departamento, pk=departamento_id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento actualizado correctamente')
        else:
            errors=form.errors
            return render(request, 'departamento/edit.html',{'errors': errors, 'departamento':departamento})
        
    return redirect('/departamento')

def store_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento Guardado correctamente')
        else:
            errors=form.errors
            data=form.data
            return render(request, 'departamento/create.html',{'errors': errors, 'data': data})
           
    return redirect('/departamento')

def delete_departamento(request, departamento_id):
    departamento =  get_object_or_404(Departamento, pk=departamento_id)
    try:
        departamento.delete()
        messages.success(request, 'Departamento Borrado correctamente')
    except:
        messages.error(request, 'Este Departamento tiene Municipios asignados')
    

    return redirect('/departamento')
"""
