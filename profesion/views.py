from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import Profesion
from .forms import ProfesionForm

# Create your views here.
def index_profesion(request):
    profesiones_list = Profesion.objects.all().order_by('nombre')
    return render(request, 'profesion/index.html', {'profesiones_list': profesiones_list})

def create_profesion(request):
    return render(request, 'profesion/create.html')

def edit_profesion(request, profesion_id):
    profesion = get_object_or_404(Profesion,pk=profesion_id)
    return render(request, 'profesion/edit.html', {'profesion': profesion})

def update_profesion(request, profesion_id):
    profesion =  get_object_or_404(Profesion, pk=profesion_id)
    if request.method == 'POST':
        form = ProfesionForm(request.POST, instance=profesion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profesión actualizada correctamente')
        else:
            errors=form.errors
            return render(request, 'profesion/edit.html',{'errors': errors, 'profesion':profesion})
       
    return redirect('/profesion')

def store_profesion(request):
    if request.method == 'POST':
        form = ProfesionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profesión Guardada correctamente')
        else:
            errors=form.errors
            data=form.data
            return render(request, 'profesion/create.html',{'errors': errors, 'data': data})
            
    return redirect('/profesion')

def delete_profesion(request, profesion_id):
    profesion =  get_object_or_404(Profesion, pk=profesion_id)
    try:
        profesion.delete()
        messages.success(request, 'Profesion Borrado correctamente')
    except:
        messages.error(request, 'Profesion esta asignado a empleados')

    return redirect('/profesion')
    