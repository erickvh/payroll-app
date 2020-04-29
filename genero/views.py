from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
#imports del modelo
from .models import Genero
from .forms import GeneroForm

# Create your views here.
def index_genero(request):
    genero_list = Genero.objects.all().order_by('nombre')
    return render(request, 'genero/index.html', {'genero_list': genero_list})

def create_genero(request):
    return render(request, 'genero/create.html')

def edit_genero(request, genero_id):
    genero = get_object_or_404(Genero,pk=genero_id)
    return render(request, 'genero/edit.html', {'genero': genero})

def update_genero(request, genero_id):
    genero =  get_object_or_404(Genero, pk=genero_id)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            messages.success(request, 'Genero Actualizado correctamente')
        else:
            errors=form.errors
            return render(request, 'genero/edit.html',{'errors': errors, 'genero':genero})

    return redirect('/genero')

def store_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Genero Guardado correctamente')
        else:
            errors=form.errors
            data=form.data
            return render(request, 'genero/create.html',{'errors': errors,'data': data})
    return redirect('/genero')

def delete_genero(request, genero_id):
    genero =  get_object_or_404(Genero, pk=genero_id)
    genero.delete()
    messages.success(request, 'Genero Borrado correctamente')

    return redirect('/genero')


    