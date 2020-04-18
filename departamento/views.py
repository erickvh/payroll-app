# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import Departamento
from .forms import DepartamentoForm

# Create your views here.
def index_departamento(request):
    departamento_list = Departamento.objects.all().order_by('nombre')
    paginator = Paginator(departamento_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'departamento/index.html', {'page_obj': page_obj})

def create_departamento(request):
    return render(request, 'departamento/create.html')

def edit_departamento(request, departamento_id):
    departamento = get_object_or_404(Departamento,pk=departamento_id)
    context = {'departamento': departamento}
    return render(request, 'departamento/edit.html', context)
   
def update_departamento(request, departamento_id):
    departamento =  get_object_or_404(Departamento, pk=departamento_id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        form.save()
        messages.success(request, 'Departamento actualizado correctamente')
    return redirect('/departamento')

def store_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento Guardado correctamente')
    return redirect('/departamento')


    