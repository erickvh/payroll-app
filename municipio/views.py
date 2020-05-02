from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages

from .models import Municipio
from departamento.models import Departamento
from .forms import MunicipioForm

def index_municipio(request):
    municipio_list = Municipio.objects.all().order_by('nombre')
    return render(request, 'municipio/index.html', {'municipio_list': municipio_list})

def create_municipio(request):
	departamento_list = Departamento.objects.all().order_by('nombre')
	return render(request, 'municipio/create.html', {'departamento_list': departamento_list})

def store_municipio(request):
    if request.method == 'POST':
        form = MunicipioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Municipio Guardado correctamente')
        else:
            errors=form.errors
            data=form.data
            departamento_list = Departamento.objects.all().order_by('nombre')
            return render(request, 'municipio/create.html',{'errors': errors, 'data': data, 'departamento_list': departamento_list})
           
    return redirect('/municipio')

def edit_municipio(request, municipio_id):
    municipio = get_object_or_404(Municipio,pk=municipio_id)
    departamento_list = Departamento.objects.all().order_by('nombre')
    return render(request, 'municipio/edit.html', {'municipio': municipio,'departamento_list': departamento_list})
   
def update_municipio(request, municipio_id):
    municipio =  get_object_or_404(Municipio, pk=municipio_id)
    departamento_list = Departamento.objects.all().order_by('nombre')
    if request.method == 'POST':
        form = MunicipioForm(request.POST, instance=municipio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Municipio actualizado correctamente')
        else:
            errors=form.errors
            return render(request, 'Municipio/edit.html',{'errors': errors, 'municipio':municipio,'departamento_list': departamento_list})
        
    return redirect('/municipio')


def delete_municipio(request, municipio_id):
    municipio =  get_object_or_404(Municipio, pk=municipio_id)
    municipio.delete()
    messages.success(request, 'Municipio Borrado correctamente')
    return redirect('/municipio')
