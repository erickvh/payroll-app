from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import EstadoCivil
from .forms import EstadoCivilForm

# Create your views here.
def index_estado(request):
    estado_civil_list = EstadoCivil.objects.all().order_by('nombre')
    return render(request, 'estado_civil/index.html', {'estado_civil_list': estado_civil_list})

def create_estado(request):
    return render(request, 'estado_civil/create.html')

def edit_estado(request, estado_id):
    estado_civil = get_object_or_404(EstadoCivil,pk=estado_id)
    context = {'estado_civil': estado_civil}
    return render(request, 'estado_civil/edit.html', context)
   

def update_estado(request, estado_id):
    estado_civil =  get_object_or_404(EstadoCivil, pk=estado_id)
    if request.method == 'POST':
        form = EstadoCivilForm(request.POST, instance=estado_civil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estado Civil actualizado correctamente')
        else:
            errors=form.errors
            return render(request, 'estado_civil/edit.html',{'errors': errors, 'estado_civil':estado_civil})
        
    return redirect('/estadocivil')

def store_estado(request):
    if request.method == 'POST':
        form = EstadoCivilForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estado Civil Guardado correctamente')
        else:
            errors=form.errors
            data=form.data
            return render(request, 'estado_civil/create.html',{'errors': errors, 'data': data})
           
    return redirect('/estadocivil')

    