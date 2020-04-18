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
    paginator = Paginator(estado_civil_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'estado_civil/index.html', {'page_obj': page_obj})

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
        form.save()
        messages.success(request, 'Estado Civil actualizado correctamente')
    return redirect('/estadocivil')

def store_estado(request):
    if request.method == 'POST':
        form = EstadoCivilForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estado Civil Guardado correctamente')
    return redirect('/estadocivil')

    