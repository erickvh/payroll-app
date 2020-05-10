from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import Comision
from .forms import ComisionForm

# Create your views here.
def index_comision(request):
    comision_list = Comision.objects.all().order_by('id')
    return render(request, 'comision/index.html', {'comision_list': comision_list})

def create_comision(request):
    return render(request, 'comision/create.html')

def store_comision(request):
    if request.method == 'POST':
        form = ComisionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comision Guardada correctamente')
        else:
            errors=form.errors
            data=form.data
            return render(request, 'comision/create.html',{'errors': errors, 'data': data})
            
    return redirect('/comision')


def edit_comision(request,comision_id):
    comision = get_object_or_404(Comision,pk=comision_id)
    return render(request, 'comision/edit.html', {'comision': comision})

def update_comision(request, comision_id):
    comision =  get_object_or_404(Comision, pk=comision_id)
    if request.method == 'POST':
        form = ComisionForm(request.POST, instance=comision)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comision actualizada correctamente')
        else:
            errors=form.errors
            return render(request, 'comision/edit.html',{'errors': errors, 'comision':comision})
    return redirect('/comision')


def delete_comision(request, comision_id):
    comision =  get_object_or_404(Comision, pk=comision_id)
    try:
        comision.delete()
        messages.success(request, 'Comision Borrada correctamente')
    except:
        messages.error(request, 'No se puede borrar la comision')

    return redirect('/comision')

