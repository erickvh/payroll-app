from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from centro_costo.models import CentroCostos
from departamento_organizacion.models import DepartamentoOrganizacion
from .forms import CentroCostosForm


# Create your views here.
def index_centro_costos(request):
    centro_costos_list = CentroCostos.objects.all()
    return render(request, 'centro_costo/index.html', {'centro_costos': centro_costos_list})


def create_centro_costo(request):
    departamento_organizacion_list = DepartamentoOrganizacion.objects.all()
    return render(request, 'centro_costo/create.html', {'departamento_organizacion': departamento_organizacion_list})


def store_centro_costo(request):
    if request.method == 'POST':
        form = CentroCostosForm(request.POST)
        departamento_organizacion_list = DepartamentoOrganizacion.objects.all()
        if form.is_valid():
            form.save()
            messages.success(request, 'Centro de costos Guardado correctamente')
        else:
            errors = form.errors
            data = form.data
            return render(request, 'centro_costo/create.html',
                          {'errors': errors, 'data': data, 'departamento_organizacion': departamento_organizacion_list})
    return redirect('/centro_costo')


def edit_centro_costo(request, centro_costo_id):
    centro_costo = get_object_or_404(CentroCostos, pk=centro_costo_id)
    departamento_organizacion_list = DepartamentoOrganizacion.objects.all().order_by('nombre')
    return render(request, 'centro_costo/edit.html',
                  {'centro_costo': centro_costo,
                   'departamento_organizacion_list': departamento_organizacion_list})


def update_centro_costo(request, centro_costo_id):
    centro_costo = get_object_or_404(CentroCostos, pk=centro_costo_id)
    departamento_organizacion_list = DepartamentoOrganizacion.objects.all().order_by('nombre')
    if request.method == 'POST':
        form = CentroCostosForm(request.POST, instance=centro_costo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Centro de Costos actualizado correctamente')
        else:
            errors = form.errors
            return render(request, 'centro_costo/edit.html',
                          {'errors': errors, 'centro_costo': centro_costo,
                           'departamento_organizacion_list': departamento_organizacion_list})
    return redirect('/centro_costo')


def delete_centro_costo(request, centro_costo_id):
    centro_costo = get_object_or_404(CentroCostos, pk=centro_costo_id)
    centro_costo.delete()
    messages.success(request, 'El Centro de Costo ha sido Borrado correctamente')
    return redirect('/centro_costo')
