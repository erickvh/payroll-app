from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import Configuracion
from .forms import ConfiguracionForm

# Create your views here.
def edit_configuracion(request, queryset=None):
    configuracion = Configuracion.objects.filter(id=1).first()
    return render(request, 'configuracion/edit.html', {'configuracion': configuracion})

def update_configuracion(request, queryset=None):
    if (Configuracion.objects.filter(id=1).exists()):
        configuracion = Configuracion.objects.filter(id=1).first()
        if request.method == 'POST':
            formActualizar = ConfiguracionForm(request.POST, instance=configuracion)
            formActualizar.save()
            messages.success(request, 'Configuración actualizada correctamente')
    else:
        if request.method == 'POST':
            form = ConfiguracionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Configuración Guardada correctamente')
    
    return redirect('/configuracion')