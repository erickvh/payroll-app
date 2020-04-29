from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import TipoUnidad
from .forms import TipoUnidadForm

# Create your views here.
def index_unidad(request):
    tipo_unidad_list = TipoUnidad.objects.all().order_by('nombre')
    return render(request, 'tipo_unidad/index.html', {'tipo_unidad_list': tipo_unidad_list})
    
def create_unidad(request):
    return render(request, 'tipo_unidad/create.html')

def store_unidad(request):
    if request.method == 'POST':
        form = TipoUnidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo Unidad Guardado correctamente')
        else:
            errors=form.errors
            data=form.data
            return render(request, 'tipo_unidad/create.html',{'errors': errors, 'data': data})
            
    return redirect('/tipounidad')

def edit_unidad(request, unidad_id):
    tipo_unidad = get_object_or_404(TipoUnidad,pk=unidad_id)
    context = {'tipo_unidad': tipo_unidad}
    return render(request, 'tipo_unidad/edit.html', context)
   

def update_unidad(request, unidad_id):
    tipo_unidad =  get_object_or_404(TipoUnidad, pk=unidad_id)
    if request.method == 'POST':
        form = TipoUnidadForm(request.POST, instance=tipo_unidad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo Unidad actualizado correctamente')
        else:
            errors=form.errors
            return render(request, 'tipo_unidad/edit.html',{'errors': errors, 'tipo_unidad':tipo_unidad})
       
    return redirect('/tipounidad')

def delete_unidad(request, unidad_id):
    tipo_unidad =  get_object_or_404(TipoUnidad, pk=unidad_id)
    tipo_unidad.delete()
    messages.success(request, 'Tipo Unidad Borrado correctamente')

    return redirect('/tipounidad')
