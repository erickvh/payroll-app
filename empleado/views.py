# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
#imports del modelo
from .models import Empleado
#from .forms import EmpleadoForm

# Create your views here.
def index_empleado(request):
    empleado_list = Empleado.objects.all().order_by('nombre')
    return render(request, 'empleado/index.html', {'empleado_list': empleado_list})
"""
def create_departamento(request):
    return render(request, 'departamento/create.html')

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
