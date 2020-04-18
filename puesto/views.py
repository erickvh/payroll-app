from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import Puesto
from .forms import PuestoForm

# Create your views here.
def index_puesto(request):
    puesto_list = Puesto.objects.all().order_by('nombre')
    paginator = Paginator(puesto_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'puesto/index.html', {'page_obj': page_obj})

def create_puesto(request):
    return render(request, 'puesto/create.html')

def edit_puesto(request,puesto_id):
    puesto = get_object_or_404(Puesto,pk=puesto_id)
    return render(request, 'puesto/edit.html', {'puesto': puesto})

def update_puesto(request, puesto_id):
    puesto =  get_object_or_404(Puesto, pk=puesto_id)
    if request.method == 'POST':
        form = PuestoForm(request.POST, instance=puesto)
        form.save()
        messages.success(request, 'Puesto actualizado correctamente')
    return redirect('/puesto')

def store_puesto(request):
    if request.method == 'POST':
        form = PuestoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Puesto Guardada correctamente')
    return redirect('/puesto')