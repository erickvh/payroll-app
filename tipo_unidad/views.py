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
    paginator = Paginator(tipo_unidad_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tipo_unidad/index.html', {'page_obj': page_obj})
    
def create_unidad(request):
    return render(request, 'tipo_unidad/create.html')

def store_unidad(request):
    if request.method == 'POST':
        form = TipoUnidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo Unidad Guardado correctamente')
    return redirect('/tipounidad')

def edit_unidad(request, unidad_id):
    tipo_unidad = get_object_or_404(TipoUnidad,pk=unidad_id)
    context = {'tipo_unidad': tipo_unidad}
    return render(request, 'tipo_unidad/edit.html', context)
   

def update_unidad(request, unidad_id):
    tipo_unidad =  get_object_or_404(TipoUnidad, pk=unidad_id)
    if request.method == 'POST':
        form = TipoUnidadForm(request.POST, instance=tipo_unidad)
        form.save()
        messages.success(request, 'Estado Civil actualizado correctamente')
    return redirect('/tipounidad')
