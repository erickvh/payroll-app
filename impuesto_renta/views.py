from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
#imports del modelo
from .models import ImpuestoRenta
from .forms import RentaForm

# Create your views here.
def index_renta(request):
    renta_list = ImpuestoRenta.objects.all().order_by('id')
    return render(request, 'impuesto_renta/index.html', {'renta_list': renta_list})

def edit_renta(request,renta_id):
    renta = get_object_or_404(ImpuestoRenta,pk=renta_id)
    return render(request, 'impuesto_renta/edit.html', {'renta': renta})

def update_renta(request, renta_id):
    renta = get_object_or_404(ImpuestoRenta,pk=renta_id)
    if request.method == 'POST':
        form = RentaForm(request.POST, instance=renta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Impuesto de Renta actualizado correctamente')
        else:
            errors=form.errors
            return render(request, 'impuesto_renta/edit.html',{'errors': errors, 'renta':renta})
    return redirect('/renta')
